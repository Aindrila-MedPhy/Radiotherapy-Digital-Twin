import sys
import os

sys.path.append(os.path.abspath(".."))
from src.P9_digital_twin_update import DigitalTwinUpdate

twin = DigitalTwinUpdate(gain=0.6)

result = twin.update(
    predicted=0.191,
    observed=0.239
)

for k,v in result.items():

    print(k,":",v)
