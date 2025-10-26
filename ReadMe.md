# UPBGE - Mouse Helper

A python module that helps with mouse in UPBGE.

## About

This module basically "adds" two new features to the UPBGE mouse, which are: the "deltaPosition" attribute and the "reCenter" method.

The "deltaPosition" attribute, as the name suggests, refers to the delta position of the mouse, that is, how much the mouse moved between the previous frame and the current frame. This is very useful, for example, to create camera movements, the famous mouse look, which is essential for any FPS game.

The "reCenter" method refers to centering the mouse cursor in the window, which is also essential for FPS games, to prevent the cursor from leaving the window and ending up creating a frustrating experience for the user.

In this version you receive a vector of size 2 (vec2) in return from deltaPosition, which is something more interesting than just a tuple that you must access using square brackets.

## Code Example

you should be able to use Mouse Helper as follows:

```python
from PyMouse import mouse

# get the mouse delta position
delta = mouse.deltaPosition

# set the mouse cursor to the center of the window
mouse.reCenter()
```

Through the "mouse" instance of PyMouse you can still access the attributes and methods of the SCA_PythonMouse class normally, as you would with "bge.logic.mouse", example:

```python
from PyMouse import mouse

# set the cursor to invisible
mouse.visible = False
```
