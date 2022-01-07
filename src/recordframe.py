import tkinter as tk


class RecordFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.text = tk.Text(self)
        self.text.pack()
