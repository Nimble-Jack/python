from enum import Enum


class Car(Enum):
    model = 'toyota'
    doors = '4'

    class Power(Enum):
        m_type = 'gas'
        storage = 'battery'
        amount = 'giga watts'

for item in Car:
    print(item)

print(Car.Power.m_type.value)

"""
This doesnt work, try not to use it
"""