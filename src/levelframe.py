import tkinter as tk


class LevelFrame(tk.Frame):
    def __init__(self, parent, **kw):
        tk.Frame.__init__(self, parent, **kw)

        self.lvl_label = tk.Label(self, text='Level')
        self.lvl_label.pack(side=tk.LEFT)

        self._level = tk.Scale(self, from_=1, to=3,
                               orient=tk.HORIZONTAL)
        self._level.pack(side=tk.RIGHT)

    def get_level(self) -> int:
        return self._level.get()

    def set_level(self, lvl: int) -> None:
        self._level.set(lvl)
