""" Helper functions for actions on the log page.

__author__ = Nick Vazquez
__created__ = 2021-12-27
"""
from tkinter import Entry


# These 2 functions from
# https://stackoverflow.com/questions/45966876/replace-python-tkinter-label-widget-with-entry-widget
def replace_with_entry(event):
    """Overlays an Entry widget on top of an already existing widget.
    Limited to use on Label widgets due to setting constraints.
    # TODO: The above isn't true. If you're able to find the type of the
        event you may be able to validate the event type as a label.

    :param event: Event passed from a tkinter action. (?)
    :type event: ? (Try to find it with a debugger!)
    """
    # Capture the widget the event was fired from.
    widget = event.widget
    # Create an Entry widget with the widget as the parent.
    entry_widget = Entry(widget)
    # Overlay the newly created Entry widget on top of the widget.
    # The parameters are a way of making sure the overlaid widget takes up the
    # whole space. See more about that here:
    # https://www.tutorialspoint.com/python/tk_place.htm
    entry_widget.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0)
    # When the enter key is pressed (only when in focus), run remove_entry.
    entry_widget.bind("<Return>", remove_entry)
    # Finally set the focus so the binding works
    entry_widget.focus_set()


def remove_entry(event) -> None:
    """
    Removes the entry widget that fired the event. Requires that the parent
    widget be a Label.
    # TODO: Validation on this, if possible.

    :param event: Event fired from Entry widget housed in Label widget.
    :type event: ?
    :return: None
    :rtype: None
    """
    entry: Entry = event.widget
    label = entry.place_info()["in"]
    # label.configure(text=)
    lbl_var = label.cget("textvariable")
    lbl_var.set(entry.get())
    entry.destroy()
