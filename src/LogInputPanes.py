"""Pane for user input with a message and a criticality. Has a log button
that when called, will output the logged message to
"""
import logging
import sys
import tkinter as tk
from typing import Optional


class LogInputPane(tk.Frame):
    """Basic input frame for a log. Abstract class to device any type of
    frame used to create log messages.
    """
    def __init__(self, parent, logger: Optional[logging.Logger], *args,
                 **kwargs):
        super(LogInputPane, self).__init__(parent, *args, **kwargs)
        self.logger = logger

    def log(self, level, msg):
        """Run when the frame would like to log against the output endpoint.
        Adds the log to the endpoint queue.
        """
        if self.logger:
            self.logger.log(level, msg)
        else:
            logging.log(level, msg)


class MessageInputPane(LogInputPane):
    """LogInputPane that allows the user to input a text message and
    criticality."""
    def __init__(self, parent, *args,
                 **kwargs):
        super(MessageInputPane, self).__init__(parent, *args, **kwargs)
        self.message_var = tk.StringVar(self)
        self.crit_var = tk.IntVar(self)

        message_label = tk.Label(self, text='Message:')
        criticality_label = tk.Label(self, text='Criticality:')
        message_entry = tk.Entry(self, textvariable=self.message_var)
        criticality_slider = tk.Scale(self, variable=self.crit_var,
                                      orient=tk.HORIZONTAL, from_=1, to=5)
        log_btn = tk.Button(self, text='Log', command=self.log)

        message_label.grid(row=0, column=0, sticky='nsew')
        message_entry.grid(row=0, column=1, sticky='nsew')
        criticality_label.grid(row=1, column=0, sticky='nsew')
        criticality_slider.grid(row=1, column=1, sticky='nsew')
        log_btn.grid(row=2, column=1, sticky=tk.E)

    def log(self, level=None, msg=None):
        """Overrides LogInputPane.log() with criticality added."""
        if not level:
            level = self.crit_var.get() * 10
        if not msg:
            msg = self.message_var.get()
        super(MessageInputPane, self).log(level, msg)


class DataInputPane(LogInputPane):
    """Allows the user to input key:value data to a dedicated data queue."""
    def __init__(self, parent, *args, **kwargs):
        super(DataInputPane, self).__init__(parent, *args, **kwargs)


if __name__ == '__main__':
    tkinter_root = tk.Tk()
    logging.basicConfig(level=logging.DEBUG)

    logging_root = logging.getLogger()

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logging_root.addHandler(handler)
    mip = MessageInputPane(tkinter_root, logger=logging_root)
    mip.pack()
    tkinter_root.mainloop()
