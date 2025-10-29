import bge
from . import decorators

if hasattr(bge, "logic"):
    from . import delta_time
    from .mouse import PyMouse
    from .keyboard import PyKeyboard

    mouse = PyMouse()
    keyboard = PyKeyboard()
