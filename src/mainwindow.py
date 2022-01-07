import tkinter as tk

from helpwindow import HelpWindow
from levelframe import LevelFrame
from messageframe import MessageFrame


class MainWindow(tk.Frame):
    def __init__(self, parent, log_command, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)
        self.parent = parent
        self.log_command = log_command

        self.help = tk.Button(self, bitmap='info', command=self.help_window)
        self.help.pack(side=tk.RIGHT)

        # Message Section
        self.msg_frame = MessageFrame(self, self.create_message)
        self.msg_frame.pack()

        self.record_frame = tk.Frame(self)
        self.record_frame.pack(side=tk.LEFT)

    def help_window(self):
        help_window = HelpWindow(self)

    def create_message(self, level=None):
        if not level:
            level = self.msg_frame.lvl_frame.get_level()
        message = self.msg_frame.get_entry()
        self.log_command(message, level)
        self.msg_frame.clear_entry()

    def set_level_slider(self, lvl: int) -> None:
        self.msg_frame.lvl_frame.set_level(lvl)

    def get_message(self) -> str:
        return self.msg_frame.get_entry()


if __name__ == "__main__":
    def log(msg, lvl):
        print(f'{lvl}: {msg}')

    w = tk.Tk()
    main_window = MainWindow(w, log)
    main_window.pack()
    w.mainloop()