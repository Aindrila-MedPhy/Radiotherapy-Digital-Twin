import sys
import os

sys.path.append(os.path.abspath(".."))

from src.P1_tumor_growth import GompertzModel
import matplotlib.pyplot as plt

model = GompertzModel()

time, volume = model.simulate()

plt.plot(time, volume)

plt.xlabel("Time (days)")
plt.ylabel("Tumor Volume")

plt.title("Gompertz Tumor Growth")

plt.grid(True)

plt.show()
