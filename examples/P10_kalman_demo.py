import sys
import os

sys.path.append(os.path.abspath(".."))

from src.P10_kalman_filter import KalmanFilter1D

kf = KalmanFilter1D(
    process_variance=0.01,
    measurement_variance=0.04
)

kf.initialize(initial_volume=2.5)

prediction = 0.191
measurement = 0.239

result = kf.update(
    prediction,
    measurement
)

print()

for key, value in result.items():

    print(f"{key:22s}: {value:.4f}")
