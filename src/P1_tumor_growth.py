"""
tumor_growth.py

Simple Gompertz tumour growth model.
"""

import numpy as np
import matplotlib.pyplot as plt


class GompertzModel:

    def __init__(self,
                 V0=1.0,
                 growth_rate=0.03,
                 carrying_capacity=100):

        self.V0 = V0
        self.r = growth_rate
        self.K = carrying_capacity

    def simulate(self,
                 total_days=200,
                 dt=1):

        time = np.arange(0, total_days + dt, dt)

        volume = np.zeros(len(time))

        volume[0] = self.V0

        for i in range(len(time)-1):

            dV = self.r * volume[i] * np.log(self.K / volume[i])

            volume[i+1] = volume[i] + dV * dt

        return time, volume
