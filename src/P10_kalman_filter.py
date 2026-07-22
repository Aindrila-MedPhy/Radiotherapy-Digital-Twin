"""
kalman_filter.py

One-dimensional Kalman Filter for adaptive tumour tracking.
"""

import numpy as np


class KalmanFilter1D:

    def __init__(self,
                 process_variance=0.01,
                 measurement_variance=0.04):

        # Process noise (model uncertainty)
        self.Q = process_variance

        # Measurement noise (MRI uncertainty)
        self.R = measurement_variance

        # Initial estimation uncertainty
        self.P = 1.0

        # State estimate
        self.x = None

    def initialize(self, initial_volume):

        self.x = initial_volume

    def update(self, prediction, measurement):

        # -----------------------------
        # Prediction step
        # -----------------------------

        self.x = prediction

        self.P = self.P + self.Q

        # -----------------------------
        # Kalman Gain
        # -----------------------------

        K = self.P / (self.P + self.R)

        # -----------------------------
        # Innovation
        # -----------------------------

        innovation = measurement - self.x

        # -----------------------------
        # Update state
        # -----------------------------

        self.x = self.x + K * innovation

        # -----------------------------
        # Update uncertainty
        # -----------------------------

        self.P = (1 - K) * self.P

        return {

            "Prediction": prediction,

            "Measurement": measurement,

            "Innovation": innovation,

            "Kalman_Gain": K,

            "Updated_State": self.x,

            "Updated_Uncertainty": self.P

        }
