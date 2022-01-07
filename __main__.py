import logging
import logging.config
import pathlib
import tkinter as tk
from tkinter import font
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

import sys
import pathlib
print(sys.path)

path = pathlib.Path.cwd().joinpath('logging.conf')
print(path)
print(f"Path? {pathlib.Path.is_file(path)}")

if not pathlib.Path.is_file(path):
    logging.critical("Can't access logging path!")
    sys.exit()


# login setup:
if 'logs' not in [path.name for path in pathlib.Path.cwd().iterdir()]:
    pathlib.Path.mkdir(pathlib.Path.cwd().joinpath('logs'))

logging.config.fileConfig(path)
logger = logging.getLogger('root')
filelogger = logging.getLogger('fileLogger')
# driving logger:
window = tk.Tk()
#window.title('Driving Logger')

width = window.winfo_screenwidth()*10
height = window.winfo_screenheight()*10

window.geometry(f'{int(width)}x{int(height)}')
window.configure(background='Maroon', bd = '5')


notebook = ttk.Notebook(window)
notebook.pack(pady=20, padx= 15, expand=True)


frame1 = Frame(notebook, width=500, height=500)
frame2 = Frame(notebook, width=500, height=500)
frame3 = Frame(notebook, width=500, height=500)
frame1.configure(background='Gold', bd = '5')
frame2.configure(background='Gold', bd = '5')
frame3.configure(background='Gold', bd = '5')
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)


notebook.add(frame1, text='Driver Log')
notebook.add(frame2, text='Data')
notebook.add(frame3, text='Graph')


crit_opt = ['Not Critical', 'Crtitcal','Very Critical']
variable = tk.StringVar(window)
w = tk.OptionMenu(frame1, variable, *crit_opt)
sv = StringVar()

def allinfo():
    print(w.get())
    print(sv.get())


msglabel = tk.Label(frame1, text = 'Criticality: ',  font = ('Eras Bold ITC', 11))
msglabel.pack(pady=50, padx = 0, side= LEFT, anchor = 'n')
msglabel.configure(background='Gold', bd = '5')
# select an option box:

def change_color(choice):
    choice = variable.get()
crit_opt = ['Not Critical', 'Crtitcal','Very Critical']
variable = tk.StringVar(window)
com = ttk.Combobox(frame1, value=crit_opt)
com.set('Select criticality')
com.bind("<<ComboboxSelected>>",change_color)
com.pack(pady = 50, side= LEFT, anchor = 'n')

msglabel2 = tk.Label(frame1, text = 'Speed: ',  font = ('Eras Bold ITC', 11))
msglabel2.pack(side= LEFT, pady= 50, padx= 0, anchor = 'n')
msglabel2.configure(background='Gold', bd = '5')
msgbox2 = tk.Text(frame1, width = 15, height = 0.5)
msgbox2.pack(pady= 50,padx= 0, side= LEFT, anchor = 'n')

msglabel3 = tk.Label(frame1, text = 'Distance: ',  font = ('Eras Bold ITC', 11))
msglabel3.pack(pady=50,padx = 0, side= LEFT, anchor = 'n')
msglabel3.configure(background='Gold', bd = '5')
msgbox3 = tk.Text(frame1, width = 15, height = 0.5)
msgbox3.pack(pady=50, padx=0,  side= LEFT, anchor = 'n')

msglabel4 = tk.Label(frame1, text = 'Time: ',  font = ('Eras Bold ITC', 11))
msglabel4.pack(pady=50, padx = 0, side= LEFT, anchor= 'n')
msglabel4.configure(background='Gold', bd = '5')
msgbox4 = tk.Text(frame1, width = 15, height = 0.5)
msgbox4.pack(pady=50,padx= 0, side= LEFT, anchor = 'n')

msglabel5 = tk.Label(frame1, text = 'Date: ',  font = ('Eras Bold ITC', 11))
msglabel5.pack(pady=50, padx = 0, side= LEFT, anchor= 'n')
msglabel5.configure(background='Gold', bd = '5')
msgbox5 = tk.Text(frame1, width = 15, height = 0.5)
msgbox5.pack(pady=50,padx= 0, side= LEFT, anchor = 'n')

e = Entry(frame2, textvariable=sv, validate="focusout", validatecommand=allinfo)
e.grid()
e = Entry(frame2)
e.grid()

level_frame = tk.Frame(frame1)
level_frame.configure(background='Gold', bd = '5')
level_frame.pack()

tree=ttk.Treeview(frame2)

tree["columns"]=("one","two","three")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=300, minwidth=200)
tree.column("three", width=120, minwidth=70, stretch=tk.NO)

tree.heading("#0", text="Date",anchor=tk.W)
tree.heading("one", text="Criticality",anchor=tk.W)
tree.heading("two", text="Speed",anchor=tk.W)
tree.heading("three", text="Distance",anchor=tk.W)
tree.heading("three", text="Time",anchor=tk.W)
def clicked():
    print(variable.get())
submit_button = tk.Button(frame1, text="Submit", bd = '5', command= clicked)
submit_button.configure(background='Gold')
submit_button.pack(side = RIGHT, pady=25,padx= 10, anchor= 's')

categories = []
for i in range(1, 100):
    tree.insert('', tk.END, values=frame1)

# add data to the treeview
for contact in categories:
    tree.insert('', tk.END, values=categories)



tree.bind('<<TreeviewSelect>>', submit_button)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
def item_selected(self, event):
        for selected_item in self.tree.selection():
            self.tree.delete(selected_item)

window.mainloop()
window.mainloop()
window.mainloop()
window.mainloop()
window.mainloop()