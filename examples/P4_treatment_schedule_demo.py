import matplotlib.pyplot as plt

import sys
import os

sys.path.append(os.path.abspath(".."))
from src.P4_treatment_schedule import RadiotherapySimulator

sim = RadiotherapySimulator()

time, volume = sim.simulate()

plt.plot(time, volume)

plt.xlabel("Treatment Day")

plt.ylabel("Tumor Volume")

plt.title("Fractionated Radiotherapy Simulation")

plt.grid()

plt.show()
