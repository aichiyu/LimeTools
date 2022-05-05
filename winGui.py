"""This module including tools with GUI, working on Windows."""
import win32api
import win32con
from win10toast import ToastNotifier
toaster = ToastNotifier()

def errorC(msg):
    """Show a classic error message."""
    win32api.MessageBox(win32con.NULL, msg, "Error", win32con.MB_OK)


def infoM(info, info_title='info', blocking=False):
    """Create a modern Windows toast notification.
    blocking: if True, the function will block until the notification is closed."""
    toaster.show_toast(info_title, info, duration=5, threaded=not blocking)


def errorM(error, blocking=False):
    """Create a modern Windows toast error notification."""
    toaster.show_toast("Error", error, duration=5, threaded=not blocking)
