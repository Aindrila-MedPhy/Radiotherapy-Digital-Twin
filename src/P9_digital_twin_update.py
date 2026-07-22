"""
digital_twin_update.py

Simple digital twin state update.
"""


class DigitalTwinUpdate:

    def __init__(self,
                 gain=0.6):

        self.gain = gain

    def update(self,
               predicted,
               observed):

        innovation = observed - predicted

        updated = predicted + self.gain * innovation

        return {

            "Predicted": predicted,

            "Observed": observed,

            "Innovation": innovation,

            "Updated": updated

        }
