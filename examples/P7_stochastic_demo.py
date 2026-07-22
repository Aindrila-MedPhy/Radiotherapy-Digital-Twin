import sys
import os

sys.path.append(os.path.abspath(".."))

import matplotlib.pyplot as plt

from src.P3_virtual_patient import VirtualPatient
from src.P5_delayed_response import DelayedResponseSimulator
from src.P7_stochastic_response import StochasticResponseSimulator


# One patient
patient = VirtualPatient()

print("\nSame Virtual Patient")
patient.show()


delay = DelayedResponseSimulator(patient)

stochastic = StochasticResponseSimulator(patient)


t1, v1, living1, damaged1 = delay.simulate(
    total_days=60
)


t2, v2, living, damaged, sf = stochastic.simulate(
    total_days=60
)


plt.figure(figsize=(8,5))

plt.plot(
    t1,
    v1,
    linewidth=2,
    label="Deterministic"
)

plt.plot(
    t2,
    v2,
    linewidth=2,
    label="Stochastic"
)

plt.xlabel("Treatment Day")

plt.ylabel("Tumour Volume (cm³)")

plt.title("Effect of Stochastic Radiotherapy")

plt.grid(True)

plt.legend()

plt.show()

plt.figure(figsize=(8,5))

# Deterministic prediction
plt.plot(t1, v1, "k", linewidth=3, label="Deterministic")

# Five stochastic trajectories
for i in range(5):

    stochastic = StochasticResponseSimulator(patient)

    t, v, living, damaged, sf = stochastic.simulate(
    total_days=60
    )

    plt.plot(t, v, alpha=0.7)

plt.xlabel("Treatment Day")
plt.ylabel("Tumour Volume (cm³)")
plt.title("Multiple Stochastic Tumour Response Predictions")

plt.grid(True)
plt.legend()

plt.show()
