"""
day10_digital_twin_demo.py

Demonstration of an adaptive radiotherapy Digital Twin.

Pipeline

True Patient (Stochastic Simulator)
            ↓
      MRI Measurement
            ↓
 Mechanistic Prediction
            ↓
     Kalman Filter
            ↓
 Adaptive Replanning
"""

import sys
import os

sys.path.append(os.path.abspath(".."))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.P3_virtual_patient import VirtualPatient
from src.P7_stochastic_response import StochasticResponseSimulator
from src.P11_digital_twin import DigitalTwin


# ============================================================
# Random seed (reproducible results)
# ============================================================

np.random.seed(42)


# ============================================================
# Create virtual patient
# ============================================================

patient = VirtualPatient()

patient.show()


# ============================================================
# Ground-truth patient (stochastic)
# ============================================================

truth = StochasticResponseSimulator(patient)

(
    t,
    true_volume,
    living,
    damaged,
    sf
) = truth.simulate(total_days=60)


# ============================================================
# Synthetic MRI measurements
# ============================================================

noise_std = 0.02

measurements = true_volume + np.random.normal(
    0,
    noise_std,
    len(true_volume)
)

measurements = np.maximum(measurements, 0.0)


# ============================================================
# Digital Twin
# ============================================================

twin = DigitalTwin(
    patient=patient,
    process_noise=0.01,
    measurement_noise=noise_std**2,
    replanning_threshold=0.10      # 10 %
)


# ============================================================
# Run Digital Twin
# ============================================================

prediction_history = []

estimate_history = []

decision_history = []

relative_error_history = []

kalman_gain_history = []


print("\n==============================================================")
print(" Day | Prediction | Measurement | Kalman | Rel.Error | Decision")
print("==============================================================")


for measurement in measurements:

    result = twin.step(measurement)

    prediction_history.append(result["prediction"])

    estimate_history.append(result["estimate"])

    decision_history.append(result["decision"])

    relative_error_history.append(result["relative_error_percent"])

    kalman_gain_history.append(result["kalman_gain"])

    print(
        f"{result['day']:3d} | "
        f"{result['prediction']:10.3f} | "
        f"{result['measurement']:11.3f} | "
        f"{result['estimate']:7.3f} | "
        f"{result['relative_error_percent']:8.2f}% | "
        f"{result['decision']}"
    )


prediction_history = np.array(prediction_history)

estimate_history = np.array(estimate_history)


# ============================================================
# Plot
# ============================================================

plt.figure(figsize=(11,6))

plt.plot(
    t,
    true_volume,
    lw=3,
    label="Ground Truth"
)

plt.plot(
    t,
    prediction_history,
    "--",
    lw=2,
    label="Mechanistic Prediction"
)

plt.plot(
    t,
    estimate_history,
    lw=2,
    label="Digital Twin Estimate"
)

plt.scatter(
    t,
    measurements,
    s=25,
    label="MRI Measurement"
)


# ============================================================
# Mark replanning days
# ============================================================

replan_x = []
replan_y = []

for i, decision in enumerate(decision_history):

    if decision == "REPLAN":

        replan_x.append(t[i])
        replan_y.append(estimate_history[i])

plt.scatter(
    replan_x,
    replan_y,
    color="red",
    marker="*",
    s=180,
    zorder=10,
    label="Adaptive Replanning"
)


plt.xlabel("Treatment Day")

plt.ylabel("Visible Tumour Volume (cm³)")

plt.title(
    "Adaptive Radiotherapy Using a Digital Twin with Kalman Filter State Estimation"
)

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()

# ============================================================
# Save Digital Twin results
# ============================================================

results = pd.DataFrame({

    "Day": t,

    "Ground_Truth": true_volume,

    "MRI_Measurement": measurements,

    "Mechanistic_Prediction": prediction_history,

    "Digital_Twin_Estimate": estimate_history,

    "Kalman_Gain": kalman_gain_history,

    "Relative_Error_Percent": relative_error_history,

    "Decision": decision_history

})

os.makedirs("../results", exist_ok=True)

results.to_csv(
    "../results/DigitalTwinResults.csv",
    index=False
)

print("\nResults saved to:")
print("../results/DigitalTwinResults.csv")

# ============================================================
# Replanning summary
# ============================================================

print("\n========================================")
print("Adaptive Replanning Summary")
print("========================================")

replan_days = []

for day, decision in enumerate(decision_history):

    if decision == "REPLAN":

        replan_days.append(day)

        print(
            f"Day {day:2d}"
            f" | Relative Error = {relative_error_history[day]:.2f}%"
        )

if len(replan_days) == 0:

    print("No replanning required.")

else:

    print(f"\nTotal replans : {len(replan_days)}")
    print(f"Replan days   : {replan_days}")
