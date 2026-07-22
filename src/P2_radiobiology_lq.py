"""
radiobiology_lq.py

Linear-Quadratic (LQ) radiobiology model
"""

import numpy as np


class LinearQuadraticModel:

    def __init__(self, alpha=0.30,
                       beta=0.03):

        self.alpha = alpha
        self.beta = beta

    def surviving_fraction(self, dose):

        sf = np.exp(-(self.alpha * dose + self.beta * dose**2))

        return sf
