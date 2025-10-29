# UPBGE - PyHelper

A Python module with small functionalities to help with game development on UPBGE.

## Resources

- [x] Delta Time (Time elapsed between frames, used to maintain stability on different hardware & FPS)
- [x] Decorators (They help modify functions to achieve specific behaviors)
- [x] PyKeyboard (A class that "extends" the SCA_PythonKeyboard class from UPBGE)
- [x] PyMouse (A class that "extends" the SCA_PythonMouse class from UPBGE)
- [ ] Utils (generic stuff that help with something)

## How to use?

Here are some example codes:

### Delta Time

```python
# bge.logic.deltaTime is set when importing the module
import pyhelper

# Method:
# bge.logic.deltaTime( scaled = True )
# parameter "scaled" = is the delta time scaled by timescale?
# by default = True

delta_scaled = bge.logic.deltaTime()
delta_raw = bge.logic.deltaTime(False)

print(delta_scaled, delta_raw)
```

### PyMouse

```python
from pyhelper import mouse

print(mouse.deltaPosition) # mathutils.Vector(x,y)
```

### PyKeyboard

```python
from pyhelper import keyboard

if keyboard.WKEY.active:
    print("W key is active!")
```
