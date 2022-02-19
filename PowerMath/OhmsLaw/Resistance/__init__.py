# Resistance equations
#
# EMF (volts) ^ squared / Power (watts)
def ep(e: float, p: float) -> float:
    return e ** 2 / p

# EMF (volts) / Current (amps)
def ei(e: float, i: float) -> float:
    return e / i

# Power (watts) / Current (amps) ^ squared
def pi(p: float, i: float) -> float:
    return p / i ** 2