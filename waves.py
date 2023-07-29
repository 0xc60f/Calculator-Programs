light = 3e8
planck = 6.626e-34

def wavelength(frequency):
    return light / frequency
def energyH(wavelength):
    return light * planck / wavelength
def energyE(frequency):
    return frequency * planck
def frequency(wavelength):
    return light / wavelength

op1 = int(input("1 for wavelength\n2 for energy\n3 for frequency\n"))
while (op1 < 1) or (op1 > 3):
    print("invalid option")
    op1 = int(input("1 for wavelength\n2 for energy\n3 for frequency\n"))
if op1 == 1:
    decimal = float(input("Enter frequency decimal: "))
    finalThing = wavelength(decimal)
    print(str(finalThing))
if op1 == 2:
    op2 = int(input("1 for wavelength\n2 for frequency\n"))
    while (op2 < 1) or (op2 > 2):
        print("invalid option")
        op2 = int(input("1 for wavelength\n2 for frequency\n"))
    if op2 == 1:
        decimal2 = float(input("Enter wavelength: "))
        finalThing2 = energyH(decimal2)
        print(str(finalThing2))
    if op2 == 2:
        decimal3 = float(input("Enter frequency: "))
        finalThing3 = energyE(decimal3)
        print(str(finalThing3))
if op1 == 3:
    decimal4 = float(input("Enter wavelength: "))
    finalThing4 = frequency(decimal4)
    print(str(finalThing4))
