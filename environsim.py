import numpy as np


class Simulator:
    energy_usage = 0
    average_energy = 0
    current_heat = 0
    outdoor_heat = 0
    heat_latency = 0
    heat_rate = 0
    t = 0

    def __init__(self, latency, heat_rate):
        self.heat_latency = latency
        self.heat_rate = heat_rate
        self.current_heat = np.random.randint(0, 1000)
        self.outdoor_heat = 0
        self.energy_usage = 0
        self.average_energy = 0
        self.t = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_heat += np.random.normal(0, 10)
        self.updateEnergy()
        return self

    def updateEnergy(self):
        self.t += 1
        self.average_energy = self.energy_usage / self.t

    def heat(self):
        self.current_heat += np.random.normal(self.heat_rate, 1)
        self.energy_usage += np.random.normal(self.heat_rate * 10, 0.5)
        self.updateEnergy()

    def cool(self):
        self.current_heat -= np.random.normal(self.heat_rate, 1)
        self.energy_usage += np.random.normal(self.heat_rate * 10, 0.5)
        self.updateEnergy()



