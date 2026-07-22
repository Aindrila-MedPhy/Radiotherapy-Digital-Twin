import sys
import os

sys.path.append(os.path.abspath(".."))

import matplotlib.pyplot as plt

from src.P3_virtual_patient import VirtualPatient
from src.P5_delayed_response import DelayedResponseSimulator
from src.P6_accelerated_repopulation import AcceleratedRepopulationSimulator


# -------------------------------------------------
# Create ONE virtual patient
# -------------------------------------------------

patient = VirtualPatient()

print("\nUsing the SAME Virtual Patient")
patient.show()


# -------------------------------------------------
# Simulate delayed response
# -------------------------------------------------

delay = DelayedResponseSimulator(patient)

t1, visible1, living1, damaged1 = delay.simulate(
    total_days=60
)


# -------------------------------------------------
# Simulate accelerated repopulation
# -------------------------------------------------

repo = AcceleratedRepopulationSimulator(patient)

t2, v2 = repo.simulate(total_days=60)


# -------------------------------------------------
# Plot
# -------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    t1,
    visible1,
    linewidth=2,
    label="Delayed Response"
)

plt.plot(
    t2,
    v2,
    linewidth=2,
    label="Accelerated Repopulation"
)

plt.xlabel("Treatment Day")
plt.ylabel("Visible Tumour Volume (cm³)")
plt.title("Effect of Accelerated Repopulation")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
