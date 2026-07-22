"""
digital_twin.py

Digital Twin framework for adaptive radiotherapy.

Workflow

Mechanistic Model
        ↓
Prediction
        ↓
MRI Measurement
        ↓
Kalman Filter
        ↓
Digital Twin Update
        ↓
Adaptive Replanning
"""

import numpy as np

import sys
import os

sys.path.append(os.path.abspath(".."))
from src.P5_delayed_response import DelayedResponseSimulator
from src.P10_kalman_filter import KalmanFilter1D
from src.P8_adaptive_replanning import AdaptiveReplanning


class DigitalTwin:

    def __init__(self,
                 patient,
                 process_noise=0.02,
                 measurement_noise=0.01,
                 replanning_threshold=0.15):

        self.patient = patient

        self.model = DelayedResponseSimulator(patient)

        self.kalman = KalmanFilter1D(
            process_variance=process_noise,
            measurement_variance=measurement_noise
        )

        self.replanner = AdaptiveReplanning(
            threshold=replanning_threshold
        )

        # Initial tumour state
        self.living = self.model.growth.V0
        self.damaged = 0.0

        self.day = 0

    # ======================================================
    # One Digital Twin update
    # ======================================================

    def step(self, measurement):

        # --------------------------------------------
        # 1. Mechanistic prediction
        # --------------------------------------------

        self.living, self.damaged, prediction = self.model.step(
            living=self.living,
            damaged=self.damaged,
            day=self.day
        )

        prediction = max(prediction, 1e-6)

        # --------------------------------------------
        # 2. Kalman Filter
        # --------------------------------------------

        kalman_result = self.kalman.update(
            prediction=prediction,
            measurement=measurement
        )

        estimate = kalman_result["Updated_State"]

        estimate = max(estimate, 1e-6)

        # --------------------------------------------
        # 3. Adaptive Replanning
        # Compare MODEL vs MEASUREMENT
        # --------------------------------------------

        replanning = self.replanner.compare(
            predicted_volume=prediction,
            observed_volume=measurement
        )

        # --------------------------------------------
        # 4. Update Digital Twin state
        # --------------------------------------------

        total = self.living + self.damaged

        if total > 1e-10:

            scale = estimate / total

            self.living *= scale
            self.damaged *= scale

        self.living = max(self.living, 1e-6)
        self.damaged = max(self.damaged, 0.0)

        self.day += 1

        # --------------------------------------------
        # 5. Return everything
        # --------------------------------------------

        return {

            "day": self.day,

            "prediction": prediction,

            "measurement": measurement,

            "estimate": estimate,

            "kalman_gain": kalman_result["Kalman_Gain"],

            "prediction_error": replanning["Error"],

            "absolute_error": replanning["Absolute_Error"],

            "relative_error": replanning["Relative_Error"],

            "relative_error_percent":
                replanning["Relative_Error_Percent"],

            "decision": replanning["Decision"]

        }
