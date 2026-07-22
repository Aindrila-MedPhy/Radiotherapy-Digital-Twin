import sys
import os

sys.path.append(os.path.abspath(".."))
from src.P2_radiobiology_lq import LinearQuadraticModel

model = LinearQuadraticModel()

dose = 2.0      # 2 Gy

sf = model.surviving_fraction(dose)

print("Dose:", dose, "Gy")
print("Surviving Fraction:", sf)
