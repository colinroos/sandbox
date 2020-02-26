from nest import SmartThemostat
import matplotlib.pyplot as plt
import pandas as pd


them = SmartThemostat(target=500, maxsteps=1000)
current_temp = []
current_heat = []
outdoor_heat = []
avg_energy = []
df = pd.DataFrame()

while True:
    try:
        next(them)
        current_heat.append(them.sim.current_heat)
        current_temp.append(them.sim.current_temp)
        outdoor_heat.append(them.sim.outdoor_heat)
        avg_energy.append(them.sim.average_energy)
    except StopIteration:

        df['current_heat'] = current_heat
        df['current_temp'] = current_temp
        df['outdoor_heat'] = outdoor_heat
        df['avg_energy'] = avg_energy

        fig, ax1 = plt.subplots()
        df['current_heat'].plot(ax=ax1, label='current heat')
        df['current_temp'].plot(ax=ax1, label='current temp')
        df['outdoor_heat'].plot(ax=ax1, label='outdoor heat')
        plt.legend()
        ax2 = ax1.twinx()
        df['avg_energy'].plot(ax=ax2, c='red', label='avg energy')
        plt.legend()
        plt.show()
        break
