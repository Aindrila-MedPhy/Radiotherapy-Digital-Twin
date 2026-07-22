import sys
import os

sys.path.append(os.path.abspath(".."))

import matplotlib.pyplot as plt

from src.P5_delayed_response import DelayedResponseSimulator

sim = DelayedResponseSimulator()

time, visible, living, damaged = sim.simulate(
    total_days=60,
    dose=2.0,
    clearance_rate=0.12
)

plt.figure(figsize=(8,5))

plt.plot(time, visible, linewidth=3, label="Visible Tumour")

plt.plot(time, living, "--", linewidth=2, label="Living Cells")

plt.plot(time, damaged, ":", linewidth=2, label="Damaged Cells")

plt.xlabel("Treatment Day")
plt.ylabel("Tumour Volume (cm³)")
plt.title("Delayed Tumour Response Model")

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.show()
