G = 6.67e-11
mass = float(input("Enter mass num of planet in kg: "))
radius = float(input("Enter radius of planet in m: "))
smallg = G * mass / radius**2
answer = "{:.6e}".format(smallg)
print("Small g is", answer, "m/s^2")
