import tkinter as tk

from levelframe import LevelFrame


class MessageFrame(tk.Frame):
    def __init__(self, parent, command, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.command = command

        # Message Frame #
        self._msg_frame = tk.Frame(self)

        self.msg_label = tk.Label(self._msg_frame, text='Message:')
        self.msg_label.pack(side=tk.LEFT)

        self.log_message = tk.StringVar(self._msg_frame)
        self._msg_box = tk.Entry(self._msg_frame, textvariable=self.log_message)
        self._msg_box.pack(side=tk.RIGHT)

        self._msg_frame.pack()

        # Level Scale Section
        self.lvl_frame = LevelFrame(self)
        self.lvl_frame.pack()

        # Submit Section
        self.submit_btn = tk.Button(self, text='Submit',
                                    activebackground='blue',
                                    command=self.command)
        self.submit_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True)

    def clear_entry(self) -> None:
        self._msg_box.delete(0, tk.END)

    def get_entry(self) -> str:
        return self._msg_box.get()
