#foot candles to lux
# 1 fc  = 10.76 lux


# lux is the international measurement of light
def fc2lux(fc: float) -> float:
    return fc * 10.76

# fc is the US measurment of light
def lux2fc(lux: float) -> float:
    return lux / 10.76