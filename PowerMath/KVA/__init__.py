# These formulas are from the PDF files provided for William F. White on their web site for the step-down transformers they rent out.
# their equipment is mostly used in the film industry.

# Single Phase
# KVA = (V x A )/1000
# A = (KVA X 1000)/Volts

def kva1(v:float, a:float) -> float:
    return (v * a) / 1000

def volts1(kva:float, a:float) -> float:
   return (kva * 1000) / a

def amps1(kva: float, v: float) -> float:
   return (kva * 1000) / v	


#    3 Phase KVA
#    KVA = (V x A x 1.73)/1000
#    A = (KVA X 1000)/(1.73 x Volts)

def kva3(V: float, A: float) -> float:
   return (V * A * 1.73) / 1000
   
def amps3(KVA: float, V: float) -> float:
   return (KVA * 1000) / (1.73 * V)
   
def volts3(KVA: float, A: float) -> float:
    return (KVA * 1000) / (1.73 * A)
	