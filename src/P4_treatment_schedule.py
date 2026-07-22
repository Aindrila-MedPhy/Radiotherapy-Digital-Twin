"""
treatment_schedule.py

Fractionated radiotherapy simulation
"""

import numpy as np
import sys
import os

sys.path.append(os.path.abspath(".."))

from src.P3_virtual_patient import VirtualPatient
from src.P1_tumor_growth import GompertzModel
from src.P2_radiobiology_lq import LinearQuadraticModel


class RadiotherapySimulator:

    def __init__(self):

        self.patient = VirtualPatient()

        self.growth = GompertzModel(
        self.patient.initial_volume,
        self.patient.growth_rate,
        self.patient.carrying_capacity
                                     )

        self.lq = LinearQuadraticModel(
        self.patient.alpha,
        self.patient.beta
                                      )

    def simulate(self,
                 total_days=60,
                 dose=2.0):

        self.patient.show()
        volume = self.growth.V0

        tumor_history = []

        time = []

        for day in range(total_days):

            # -----------------------------
            # Tumor growth for one day
            # -----------------------------

            dV = self.growth.r * volume * np.log(self.growth.K / volume)

            volume = volume + dV

            # -----------------------------
            # Monday-Friday treatment
            # -----------------------------

            weekday = day % 7

            if weekday < 5:

                sf = self.lq.surviving_fraction(dose)

                volume = volume * sf

            tumor_history.append(volume)

            time.append(day)

        return np.array(time), np.array(tumor_history)
