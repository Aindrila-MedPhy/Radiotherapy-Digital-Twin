import sys
import os

sys.path.append(os.path.abspath(".."))

import matplotlib.pyplot as plt

from src.P4_treatment_schedule import RadiotherapySimulator
from src.P5_delayed_response import DelayedResponseSimulator

original = RadiotherapySimulator()

t1, v1 = original.simulate(total_days=60)

improved = DelayedResponseSimulator()

t2, visible2, living2, damaged2 = improved.simulate(
    total_days=60
)

plt.figure(figsize=(8,5))

plt.plot(
    t1,
    v1,
    linewidth=2,
    label="Instant Cell Kill"
)

plt.plot(
    t2,
    visible2,
    linewidth=2,
    label="Delayed Regression"
)

plt.xlabel("Treatment Day")
plt.ylabel("Tumour Volume (cm³)")
plt.title("Comparison of Tumour Response Models")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
