#   P = E x I (Watts = Voltage x Amps)
#   E = P ÷ I (Voltage = Watts ÷ Amps)
#   I = P ÷ E (Amps = Watts ÷ Voltage)

def watts(volts: float, amps: float) -> float:
	return volts * amps
	
def volts(watts: float, amps: float) -> float:
	return watts / amps
		
def amps(watts: float, volts: float) -> float:
	return watts / volts
