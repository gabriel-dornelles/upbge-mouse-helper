import bge
import time
from .decorators import once_per_tick

class DeltaTime:
    def __init__(self):
        self.__old_clock = time.perf_counter()
        self.__delta = 0.0
    
    @once_per_tick
    def __calculate__(self, scaled):
        current_clock = time.perf_counter()
        dt = current_clock - self.__old_clock
        
        self.__delta = dt * bge.logic.getTimeScale() if scaled else dt
        self.__old_clock = current_clock
    
    def deltaTime(self, scaled = True):
        self.__calculate__(scaled)
        return self.__delta

bge.logic.deltaTime = DeltaTime().deltaTime
