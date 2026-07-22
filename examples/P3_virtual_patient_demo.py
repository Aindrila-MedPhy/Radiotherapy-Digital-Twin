
import sys
import os

sys.path.append(os.path.abspath(".."))
from src.P3_virtual_patient import VirtualPatient

for i in range(5):
    print(f"\nPatient {i+1}")
    patient = VirtualPatient()
    patient.show()
