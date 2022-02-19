# Power (Watts) equations

# Current (amps) ^ squared X Resistance (ohms) 
def ir(i: float, r: float) -> float:
    return i ** 2 * r

# Power (watts) X Current (amps)
def ei(e: float, i: float) -> float:
    return e * i

# Power (watts) ^ squared / Resistance
def er(e: float, r: float) -> float:
    return e ** 2 / r