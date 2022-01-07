import tkinter as tk
from tkinter import Entry, Frame, Label, StringVar, Button
from typing import List

import helpers.log_page as helpers


class Container(Frame):
    """Field input."""
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(Container, self).__init__(parent, *args, **kwargs)
        self.rows: List[FieldRow] = []
        self.btn = Button(self, text='Add Row', command=self.add_row)
        self.btn.grid(row=1000, column=0)

        # self.label.after(20000, helpers.replace_with_entry)
        # self.bind('<Double-Button-1>', helpers.replace_with_entry)

    def add_row(self, field_name: str = None):
        fr = FieldRow(self)
        self.rows.append(fr)
        self.update()

    def update(self) -> None:
        for index, row in enumerate(self.rows):
            row.grid(row=index, column=0)
            row.focus_set()
        return super().update()


class FieldRow(Frame):
    def __init__(self, parent, text=None, *args, **kwargs) -> None:
        self.parent = parent
        super(FieldRow, self).__init__(parent, *args, **kwargs)
        text_var = StringVar(self, value=text if text else 'VAR')
        self.btn = Label(self, textvariable=text_var)
        self.btn.grid(row=0, column=0)
        
        self.value_entry = Entry(self)
        self.value_entry.grid(row=0, column=1)

        self.bind('<Double-Button-1>', helpers.replace_with_entry)
        

if __name__ == '__main__':
    root = tk.Tk()
    f = Container(root)
    f.pack()
    f.add_row()
    root.mainloop()
