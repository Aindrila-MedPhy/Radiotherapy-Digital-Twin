"""
adaptive_replanning.py

Adaptive radiotherapy decision module based on
relative tumour volume error.
"""

import numpy as np


class AdaptiveReplanning:

    def __init__(self, threshold=0.15):
        """
        Parameters
        ----------
        threshold : float
            Relative error threshold.
            Example:
                0.15 = 15%
        """
        self.threshold = threshold

    def compare(self,
                predicted_volume,
                observed_volume):

        # ---------------------------------------
        # Prediction error
        # ---------------------------------------

        error = observed_volume - predicted_volume

        abs_error = abs(error)

        # ---------------------------------------
        # Relative error (%)
        # ---------------------------------------

        if predicted_volume > 1e-10:
            relative_error = abs_error / predicted_volume
        else:
            relative_error = 0.0

        # ---------------------------------------
        # Adaptive replanning decision
        # ---------------------------------------

        if relative_error > self.threshold:
            decision = "REPLAN"
        else:
            decision = "CONTINUE"

        # ---------------------------------------
        # Return results
        # ---------------------------------------

        return {

            "Predicted": predicted_volume,

            "Observed": observed_volume,

            "Error": error,

            "Absolute_Error": abs_error,

            "Relative_Error": relative_error,

            "Relative_Error_Percent": relative_error * 100,

            "Decision": decision

        }
