# Volatage equations
#
# square root of [ Power (watts) X Resistance (ohms) ]
def pr(p: float,r: float) -> float:
    return ( p * r ) ** .5

# Power (watts) X Current (amps)
def pi(p: float,i: float) -> float:
    return p / i

# Current (amps) X Resistance (ohms)
def ir(i: float,r: float) -> float:
    return i * r