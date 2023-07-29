mass1 = float(input("Enter mass1 num in kg: "))
mass2 = float(input("Enter mass2 num in kg: "))
distance = float(input("Enter distance in meters: "))
G = 6.67e-11
force = G * (mass1 * mass2) / distance
force = "{:.6e}".format(force)
print("Gravitational force is", force, "newtons")
