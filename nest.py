from environsim import Simulator
import numpy as np


class SmartThemostat:
    t = 0
    simsteps = 0
    target_temp = 0

    def __init__(self, target, maxsteps):
        self.t = 0
        self.sim = Simulator(latency=0.5, heat_rate=5)
        self.simsteps = maxsteps
        self.target_temp = target

    def __iter__(self):
        return self

    def __next__(self):
        if self.t < self.simsteps:
            state = next(self.sim)
            print(state.current_heat)
            if state.current_heat > self.target_temp:
                self.sim.cool()
            elif state.current_heat < self.target_temp:
                self.sim.heat()
            self.t += 1
            return self
        raise StopIteration


