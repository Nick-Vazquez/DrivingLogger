"""Tkinter application processing for a console output from a queue,
scrollable.

__author__: Nick Vazquez (nmv)
__created__: 2022/03/31
"""
import logging
import os
import queue as q

import tkinter as tk
from tkinter.scrolledtext import ScrolledText


root_logger = logging.getLogger()
logger = logging.getLogger(__name__)


class QueuedScrolledText(tk.Frame):
    """Poll messages from a logging queue and display them in a scrolled text
    widget"""

    def __init__(self, parent, queue: q.Queue, *args, **kwargs):
        """
        :param parent:
        :param queue:
        :param args:
        :param kwargs:
        """
        super().__init__(parent, *args, **kwargs)

        # Create a ScrolledText widget
        self.scrolled_text = ScrolledText(self, state='disabled', height=12)
        self.scrolled_text.pack(fill=tk.BOTH, expand=True)
        self.scrolled_text.configure(font='TkFixedFont')
        self.scrolled_text.tag_config('INFO', foreground='black')
        self.scrolled_text.tag_config('DEBUG', foreground='gray')
        self.scrolled_text.tag_config('WARNING', foreground='orange')
        self.scrolled_text.tag_config('ERROR', foreground='red')
        self.scrolled_text.tag_config('CRITICAL', foreground='red',
                                      underline=True)

        # Create a logging handler using a queue
        self.external_update_log_queue = queue
        # Find update interval and start polling messages from the queue
        self.update_interval = os.getenv('UPDATE_INTERVAL_MS', 100)
        self.after(self.update_interval, self.poll_log_queue)

    def display(self, message: str, tag=None) -> None:
        """ Updates the console output with the given message.
        Tag for highlighting.

        :param message: Message to add to the console output
        :param tag: Highlight tag (criticality) of the message.
        :type tag: str
        :return: None
        """
        self.scrolled_text.configure(state='normal')
        self.scrolled_text.insert(tk.END, message + '\n', tag)
        self.scrolled_text.configure(state='disabled')
        # Autoscroll to the bottom
        self.scrolled_text.yview(tk.END)
        self.update()

    def poll_log_queue(self):
        """Check every 100ms if there is a new message in the queue to
        display
        """
        while True:
            try:
                record: logging.LogRecord = self.external_update_log_queue.get(
                    block=False)
            except q.Empty:
                break
            else:
                self.display(root_logger.handlers[0].format(record),
                             record.levelname)
        self.after(self.update_interval, self.poll_log_queue)
