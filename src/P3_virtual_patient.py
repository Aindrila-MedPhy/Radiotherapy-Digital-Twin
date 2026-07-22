"""
virtual_patient.py

Create a virtual patient with random biological parameters.
"""

import random


class VirtualPatient:

    def __init__(self):

        # Initial tumour volume (cm^3)
        self.initial_volume = random.uniform(0.5, 3.0)

        # Gompertz growth rate
        self.growth_rate = random.uniform(0.02, 0.05)

        # Carrying capacity
        self.carrying_capacity = random.uniform(80, 120)

        # Radiobiology parameters
        self.alpha = random.uniform(0.20, 0.40)

        self.beta = random.uniform(0.02, 0.05)

    def show(self):

        print("----------------------------")
        print("Virtual Patient")
        print("----------------------------")
        print(f"Initial Volume : {self.initial_volume:.2f} cm³")
        print(f"Growth Rate    : {self.growth_rate:.3f}")
        print(f"Carrying Cap.  : {self.carrying_capacity:.1f}")
        print(f"Alpha          : {self.alpha:.3f}")
        print(f"Beta           : {self.beta:.3f}")
