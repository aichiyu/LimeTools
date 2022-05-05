"""Many tools."""
from time import time
import os

# Running time caculation.
time_in_tic_toc_func = 0
def tic()->None:
    """Return the current time in seconds."""
    global time_in_tic_toc_func
    time_in_tic_toc_func = time()


def toc(is_print:bool=True) -> float|None:
    """Return the time elapsed since tic()."""
    t = time() - time_in_tic_toc_func
    if is_print:
        print(t)
    else:
        return

# File Process.
def MakeDirValid(path:str)->str:
    """Input a dir path, return a valid dir path.
    1. Replace "\\\\" to "\\" if exists.
    2. Remove "\\" at end of a path.
    3. create this dir if not exist. """
    path = path.replace("\\\\", "\\")
    if path[-1] == "\\":
        path = path[:-1]
    if not os.path.isdir(path):
        os.makedirs(path)
    return path


# object-oriented
def StrToClass(module, classname:str)->object:
    """Given a name of a object in 'module', return this object. """
    return getattr(module, classname)
