# Amperes-Current equations
# 
# Power (watts) / EMF (volts)
def pe(p: float, e: float) -> float:
    return p / e

# EMF (volts) / Resistance (ohms)
def er(e: float, r: float) -> float:
    return e / r

# square root of [ Power (watts)/ Resistance (ohms) ]
def pr(p: float, r: float) -> float:
    # x ** .5 is square root
    return (p/r)**.5