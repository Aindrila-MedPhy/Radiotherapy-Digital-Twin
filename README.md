# Radiotherapy-Digital-Twin

A computational framework for adaptive radiotherapy featuring tumour growth modelling, radiobiological response, Kalman filter state estimation, and adaptive treatment replanning.


## Overview

In conventional radiotherapy, treatment plans are generated before the start of treatment and are generally not updated during treatment. However, tumour response varies significantly among patients due to biological heterogeneity, therapeutic response, and measurement noise.  

This project presents a computational framework for digital twin–based adaptive radiotherapy that combines mechanistic tumour modelling with simulated imaging data for continuous model updating. The framework integrates mechanistic tumour modelling Kalman filter-based estimation to improve tumour response prediction and support adaptive replanning during radiotherapy.

The entire framework is developed in Python to support research, education, and demonstration purposes.


## Features

- Gompertz tumour growth model
- Linear-Quadratic (LQ) radiobiology model
- Virtual patient generation
- Fractionated radiotherapy simulation
- Delayed tumour regression
- Accelerated tumour repopulation
- Stochastic treatment response
- Kalman filter state estimation
- Digital twin updating
- Adaptive replanning strategy

## Repository Structure
Radiotherapy-Digital-Twin/

├── src/
├── examples/
├── data/
├── results/
├── README.md
├── LICENSE
└── requirements.txt

## Simulation Workflow
Virtual Patient
        │
        ▼
Tumour Growth Model
        │
        ▼
Radiotherapy Simulation
        │
        ▼
Mechanistic Prediction
        │
        ▼
MRI Measurement
        │
        ▼
Kalman Filter
        │
        ▼
Updated Digital Twin
        │
        ▼
Adaptive Replanning


## Example Result
<p align="center">
<img src="results/DigitalTwinResults.png" width="750">
</p>

The digital twin continuously updates the mechanistic tumour model using noisy imaging measurements. Adaptive replanning is triggered whenever the relative prediction error exceeds the predefined threshold.


## Core Modules

| Module | Description |
|---------|-------------|
| tumour_growth | Gompertz tumour growth |
| radiobiology_lq | Linear-Quadratic radiobiology |
| virtual_patient | Randomized virtual patient generation |
| treatment_schedule | Fractionated radiotherapy simulation |
| delayed_response | Delayed tumour regression |
| accelerated_repopulation | Accelerated tumour repopulation |
| stochastic_response | Random treatment response |
| adaptive_replanning | Replanning decision algorithm |
| kalman_filter | State estimation |
| digital_twin | Integrated digital twin framework |


## Installation

```bash
git clone https://github.com/Aindrila-MedPhy/Radiotherapy-Digital-Twin.git

cd Radiotherapy-Digital-Twin

pip install -r requirements.txt
```

## Running an Example

```bash
python examples/P11_digital_twin_demo.py
```

## Results

Example simulation outputs are available in the **results/** folder.

These include

- Digital Twin prediction
- Mechanistic vs stochastic response
- Delayed tumour regression
- Accelerated repopulation
- Example simulation CSV


## Future Work

Potential future extensions include

- Patient-specific parameter estimation
- Extended/Unscented Kalman filtering
- Bayesian state estimation
- MRI/PET integration
- Reinforcement learning for adaptive radiotherapy
- Clinical data validation


## License

This project is released under the MIT License.
