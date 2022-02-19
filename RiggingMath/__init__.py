
# Used for dead hang calculation and bridle lenth
def leg_length(V: float, H: float) -> float:
    return (V ** 2 + H ** 2) ** .5
# Use for each leg of your hang, this is based on the horizontal axis
def leg_length_2d(Vup: float, Vdown: float, Hup: float, Hdown: float) -> float:
    return ((Vup - Vdown) ** 2 + (Hup - Hdown) ** 2) ** .5
# Use for each leg of your hang, used for a more complex hang of your rigging point
def leg_length_3d(Vup: float, Vdown: float, Hup: float, Hdown: float, Dup: float, Ddown: float) -> float:
    return ((Vup - Vdown) ** 2 + (Hup - Hdown) ** 2 + (Dup - Ddown) ** 2 ) ** .5

def DH_Tension(L: float, V: float, W: float) -> float:
    return (L / V) * W

# this is a calculation for both bridle legs above

def Tension_2leg_up_left(W: float, H1: float, H2: float, V1: float, V2: float, L: float) -> float:
    return ( W * L * H2 ) / ( ( V1 * H2 ) + ( V2 * H1 ))

def Tension_2leg_up_right(W: float, H1: float, H2: float, V1: float, V2: float, L: float) -> float:
    return ( W * L * H1 ) / ( ( V1 * H2 ) + ( V2 * H1 ))

# this is a bridle calculation for one leg up and the other tied off bellow

def Tension_2leg_updown_left(W: float, H1: float, H2: float, V1: float, V2: float, L: float) -> float:
    return ( W * L * H2 ) / ( ( V1 * H2 ) - ( V2 * H1 ))

def Tension_2leg_updown_right(W: float, H1: float, H2: float, V1: float, V2: float, L: float) -> float:
    return ( W * L * H1 ) / ( ( V1 * H2 ) - ( V2 * H1 ))


# Horizontal force

def Horizontal_force(H: float, V: float, W: float) -> float:
    return ( H / V) * W
    