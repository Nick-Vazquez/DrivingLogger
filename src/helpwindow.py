import tkinter as tk

help_text = '''
DrivingLogger is a tool to help keep track of events based on time and severity.
This tool can log messages with a criticality, view previous sessions, and
export logs to a file. Information on the use of this tool can be found on the
PrISUm Wiki. (soon...)

© PrISUm Solar Car - Fall 2021
'''


class HelpWindow(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.title('DrivingLogger Help')

        self.text = tk.Label(self, text=help_text)
        self.text.pack()
