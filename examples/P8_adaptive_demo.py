import sys
import os

sys.path.append(os.path.abspath(".."))

import pandas as pd

from src.P8_adaptive_replanning import AdaptiveReplanning


# --------------------------------------
# Read stochastic dataset
# --------------------------------------

df = pd.read_csv("virtual_patient_dataset_stochastic.csv")

patient = df[df["Patient_ID"] == 1]


# --------------------------------------
# Simulated MRI at Day 20
# --------------------------------------

day = 20

observed = patient.loc[
    patient["Day"] == day,
    "Visible_Tumour"
].values[0]


# --------------------------------------
# Assume the digital twin predicted
# a slightly different value
# --------------------------------------

predicted = observed * 0.80


# --------------------------------------
# Adaptive replanning
# --------------------------------------

planner = AdaptiveReplanning(
    threshold=0.20
)

result = planner.compare(
    predicted,
    observed
)

print()

print("Day :", day)

for key, value in result.items():

    print(key, ":", value)
