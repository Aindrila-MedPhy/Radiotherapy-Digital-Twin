"""
accelerated_repopulation.py

Delayed tumour regression +
Accelerated repopulation during radiotherapy.
"""

import numpy as np
import sys
import os

sys.path.append(os.path.abspath(".."))

from src.P3_virtual_patient import VirtualPatient
from src.P1_tumor_growth import GompertzModel
from src.P2_radiobiology_lq import LinearQuadraticModel


class AcceleratedRepopulationSimulator:

    def __init__(self, patient=None):

        if patient is None:
            self.patient = VirtualPatient()
        else:
            self.patient = patient

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
                 dose=2.0,
                 clearance_rate=0.12,
                 repopulation_day=21,
                 max_growth_multiplier=2.0):

        self.patient.show()

        living = self.growth.V0
        damaged = 0.0

        tumour_history = []
        time = []

        for day in range(total_days):

            # ------------------------------------
            # Accelerated repopulation
            # ------------------------------------

            if day < repopulation_day:

                growth_rate = self.growth.r

            else:

                progress = (day - repopulation_day) / (total_days - repopulation_day)

                growth_rate = self.growth.r * (
                    1 + (max_growth_multiplier - 1) * progress
                )

            # ------------------------------------
            # Gompertz growth
            # ------------------------------------

            dV = growth_rate * living * np.log(self.growth.K / living)

            living += dV

            # ------------------------------------
            # Monday-Friday treatment
            # ------------------------------------

            weekday = day % 7

            if weekday < 5:

                sf = self.lq.surviving_fraction(dose)

                surviving = living * sf

                newly_damaged = living - surviving

                living = surviving

                damaged += newly_damaged

            # ------------------------------------
            # Clearance
            # ------------------------------------

            damaged -= clearance_rate * damaged

            # ------------------------------------
            # Visible tumour
            # ------------------------------------

            visible = living + damaged

            tumour_history.append(visible)

            time.append(day)

        return np.array(time), np.array(tumour_history)
