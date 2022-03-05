"""Example module for logging records (Name, Value, Unit) of any quantitative
measurement in the application.
"""
import logging
import tkinter
import typing


class DataRecordWidget(tkinter.Frame):
    """ Needs a new name.

    Container that holds 3 entry fields for each
    """
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # (name of attribute to set, column weight)
        # {column: weight}
        entries = {'name': 1, 'data': 3, 'unit': 1}
        for index, (key, value) in enumerate(entries.items()):
            string_var = tkinter.StringVar(self)
            entry = tkinter.Entry(self, textvariable=string_var, width=10)
            entry.grid(row=0, column=index, sticky='we')
            self.columnconfigure(index, weight=value)
            self.__setattr__(key, string_var)

    def clear_value(self):
        """Clears out any value entered into the data field."""
        data_var: tkinter.StringVar = self.__getattribute__('data')
        data_var.set('')


class DataRecordContainer(tkinter.Frame):
    """Manages DataRecordWidget objects and contains them in a stacked form.

    Layout-type class.
    """
    def __init__(self, parent, *args, **kwargs):
        super(DataRecordContainer, self).__init__(parent, *args, **kwargs)
        self._record_list: typing.List[DataRecordWidget] = []

        self.add_button = tkinter.Button(text='+', command=self.add_record)
        self.add_button.pack()

    def add_record(self, record: DataRecordWidget = None) -> None:
        """Generates a new record object for user input.

        Needs to maintain a reference to the created object, so it adds it to
        the list of records housed in the self container.

        Updates to ensure that the newly created widget is displayed to user.
        """
        if not record:
            record = DataRecordWidget(self)
        self._record_list.append(record)
        self.update()

    def update(self) -> None:
        """Renders all records in the record_list into the self container."""
        for record in self._record_list:
            try:
                record.pack(fill=tkinter.X, expand=True)
            except tkinter.TclError as error:
                # This is excepted because when a record destroys itself, the
                # reference to the object is not removed from the container's
                # record list. We do that here.
                logging.debug('Removed a non-existent value from record_list.')
                self._record_list.remove(record)
        self.add_button.pack()
        super(DataRecordContainer, self).update()


if __name__ == '__main__':
    root = tkinter.Tk()
    rc = DataRecordContainer(root)
    rc.pack(expand=True, fill=tkinter.X)
    root.mainloop()
