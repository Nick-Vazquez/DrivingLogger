import logging
import logging.config
import pathlib
import tkinter as tk

# login setup:
if 'logs' not in [path.name for path in pathlib.Path.cwd().iterdir()]:
    pathlib.Path.mkdir(pathlib.Path.cwd().joinpath('logs'))

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')
filelogger = logging.getLogger('fileLogger')
# driving logger:
window = tk.Tk()
window.title('Driving Logger')

width = window.winfo_screenwidth()*0.75
height = window.winfo_screenheight()*0.75

window.geometry(f'{int(width)}x{int(height)}')


msglabel = tk.Label(window, text = 'Message' )
msglabel.pack()
msgbox = tk.Text(window)
msgbox.pack()

level_frame = tk.Frame(window)
level_frame.pack()

level_label = tk.Label(level_frame,text = 'Level:', padx=5)
level_label.pack(side = tk.LEFT)

#make a new frame for level and slider
#create submit button


level = tk.Scale(level_frame, from_=1, to=4, orient=tk.HORIZONTAL, padx=5)



level.pack()


window.mainloop()

