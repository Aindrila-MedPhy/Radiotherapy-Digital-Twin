"""
delayed_response.py

Radiotherapy model with delayed tumour regression.
"""

import numpy as np
import sys
import os

sys.path.append(os.path.abspath(".."))

from src.P3_virtual_patient import VirtualPatient
from src.P1_tumor_growth import GompertzModel
from src.P2_radiobiology_lq import LinearQuadraticModel


class DelayedResponseSimulator:

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

    # ==========================================================
    # One-day tumour evolution
    # ==========================================================

    def step(self,
             living,
             damaged,
             day,
             dose=2.0,
             clearance_rate=0.12):

        # --------------------------------------
        # 1. Gompertz growth
        # --------------------------------------

        dV = self.growth.r * living * np.log(self.growth.K / living)

        living += dV

        # --------------------------------------
        # 2. Monday-Friday radiotherapy
        # --------------------------------------

        weekday = day % 7

        if weekday < 5:

            sf = self.lq.surviving_fraction(dose)

            surviving = living * sf

            newly_damaged = living - surviving

            living = surviving

            damaged += newly_damaged

        # --------------------------------------
        # 3. Clearance of damaged cells
        # --------------------------------------

        damaged -= clearance_rate * damaged

        # --------------------------------------
        # 4. Visible tumour
        # --------------------------------------

        visible = living + damaged

        return living, damaged, visible

    # ==========================================================
    # Full simulation
    # ==========================================================

    def simulate(self,
                 total_days=60,
                 dose=2.0,
                 clearance_rate=0.12,
                 show_patient=False):

        if show_patient:
            self.patient.show()

        living = self.growth.V0

        damaged = 0.0

        time = []

        tumour_history = []

        living_history = []

        damaged_history = []

        for day in range(total_days):

            living, damaged, visible = self.step(
                living=living,
                damaged=damaged,
                day=day,
                dose=dose,
                clearance_rate=clearance_rate
            )

            time.append(day)

            tumour_history.append(visible)

            living_history.append(living)

            damaged_history.append(damaged)

        return (
            np.array(time),
            np.array(tumour_history),
            np.array(living_history),
            np.array(damaged_history)
        )
