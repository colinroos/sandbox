from nest import SmartThemostat
import matplotlib.pyplot as plt
import pandas as pd


them = SmartThemostat(target=500, maxsteps=1000)
temps = []
energy = []

while True:
    try:
        next(them)
        temps.append(them.sim.current_heat)
        energy.append(them.sim.average_energy)
    except StopIteration:
        df = pd.DataFrame()
        df['temps'] = temps
        df['energy'] = energy

        fig, ax1 = plt.subplots()
        df['temps'].plot(ax=ax1)
        ax2 = ax1.twinx()
        df['energy'].plot(ax=ax2, c='red')
        plt.show()
        break
