"""Frontend app for an example of a scrolled text output from a text entry."""
import logging
import os
import pathlib
import queue as q
import tkinter as tk

import LogInputPanes
import QueuedScrolledText
import helpers.Handlers as Handlers


class App(tk.Frame):
    """App in its entirely. (idk what else to put honestly)"""
    def __init__(self, parent, *args, **kwargs):
        super(App, self).__init__(parent, *args, **kwargs)

        base_dir = pathlib.Path(os.environ.get('BASE_DIR',
                                               pathlib.Path.cwd().parent))
        output_path = base_dir / 'logs' / 'outputLog.log'

        queue = q.Queue()

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        self.queue_handler = Handlers.QueueHandler(queue)
        self.file_handler = logging.FileHandler(filename=output_path)
        self.queue_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.queue_handler.setFormatter(formatter)
        self.file_handler.setFormatter(formatter)
        root_logger.addHandler(self.queue_handler)
        root_logger.addHandler(self.file_handler)

        # Actual message passing id done from the logging library end. The
        # handler added above takes
        mip = LogInputPanes.MessageInputPane(self, logger=root_logger)
        qst = QueuedScrolledText.QueuedScrolledText(self, queue)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.bind('<Control-1>', mip.log)

        mip.grid(row=0, column=0, sticky='nsew')
        qst.grid(row=0, column=1, sticky='nsew')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('PrISUm Strategy Driving Logger')
    width = root.winfo_screenwidth() * 0.5
    height = root.winfo_screenheight() * 0.5
    root.geometry(f'{int(width)}x{int(height)}')
    app = App(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
