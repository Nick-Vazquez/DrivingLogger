import pathlib
import tkinter
from tkinter import Frame, Button


class ButtonExample(Frame):
    """Example class with button in a frame and when clicked will change the
    background color."""
    def __init__(self, parent, *args, **kwargs):
        super(ButtonExample, self).__init__(parent, *args, **kwargs)



        self.btn = Button(self, text='Click me!', command=self.on_click)
        self.btn.pack()


    def on_click(self):
        """Run when the button is clicked. Changes window background color."""
        print('clicked!')


if __name__ == '__main__':
    root = tkinter.Tk()
    btn = ButtonExample(root)
    btn.pack()
    root.mainloop()
