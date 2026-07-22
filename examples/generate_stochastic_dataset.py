import sys
import os

sys.path.append(os.path.abspath(".."))

import pandas as pd

from src.P7_stochastic_response import StochasticResponseSimulator


number_of_patients = 100

all_data = []

for patient_id in range(number_of_patients):

    sim = StochasticResponseSimulator()

    (
        time,
        volume,
        living,
        damaged,
        sf
    ) = sim.simulate(total_days=60)

    patient = sim.patient

    for day in range(len(time)):

        all_data.append({

            "Patient_ID":
            patient_id + 1,

            "Day":
            int(time[day]),

            "Visible_Tumour":
            float(volume[day]),

            "Living_Tumour":
            float(living[day]),

            "Damaged_Tumour":
            float(damaged[day]),

            "Growth_Rate":
            patient.growth_rate,

            "Alpha":
            patient.alpha,

            "Beta":
            patient.beta,

            "Initial_Volume":
            patient.initial_volume,

            "Carrying_Capacity":
            patient.carrying_capacity,

            "Survival_Fraction":
            sf[day]

        })

df = pd.DataFrame(all_data)

df.to_csv(
    "virtual_patient_dataset_stochastic.csv",
    index=False
)

print(df.head())

print()

print("Dataset saved successfully!")

print("Total rows :", len(df))

print("Patients :", number_of_patients)
