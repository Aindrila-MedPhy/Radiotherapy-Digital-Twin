import sys
import os

sys.path.append(os.path.abspath(".."))

import pandas as pd

from src.P4_treatment_schedule import RadiotherapySimulator


all_data = []

number_of_patients = 100


for patient_id in range(number_of_patients):

    sim = RadiotherapySimulator()

    time, volume = sim.simulate(total_days=60)

    patient = sim.patient

    for day in range(len(time)):

        all_data.append({

            "Patient_ID": patient_id + 1,

            "Day": int(time[day]),

            "Tumor_Volume": float(volume[day]),

            "Growth_Rate": patient.growth_rate,

            "Alpha": patient.alpha,

            "Beta": patient.beta,

            "Initial_Volume": patient.initial_volume

        })


df = pd.DataFrame(all_data)

df.to_csv("virtual_patient_dataset.csv", index=False)

print(df.head())

print()

print("Dataset saved successfully!")
print("Total rows:", len(df))
