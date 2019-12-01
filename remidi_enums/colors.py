from enum import Enum


class rg_colors(Enum):
    R0G0 = 0
    R1G0 = 1
    R2G0 = 2
    R3G0 = 3
    R0G1 = 16
    R1G1 = 17
    R2G1 = 18
    R3G1 = 19
    R0G2 = 32
    R1G2 = 33
    R2G2 = 34
    R3G2 = 35
    R0G3 = 48
    R1G3 = 49
    R2G3 = 50
    R3G3 = 51

    @staticmethod
    def get_rg_value(red, green):
        if red <= 3 and green <= 3:
            return red+green*16
        else:
            raise ValueError("red("+str(red)+") or green("
                             + str(green)+") is not in allowed range: [0,3]")

    @staticmethod
    def get_rg_name(red, green):
        value = rg_colors.get_rg_value(red, green)
        rg_colors[value]

class colors(Enum):
    BLACK = rg_colors.R0G0.value
    RED = rg_colors.R3G0.value
    ORANGE = rg_colors.R2G3.value
    GREEN = rg_colors.R0G3.value
