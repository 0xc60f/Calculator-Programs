avoga = 6.022e23

def moltoatom(mol):
    return mol * avoga
def atomtomol(par):
    return par/ avoga
def atomtogram(atom, atm):
    return atom * atm / avoga   
def gramtoatom(gram, atm):
    return gram * avoga / atm
def gramtomol(gram, atm):
    return gram / atm
def moltogram(mol, gram):
    return mol * gram
def moltoliter(mol):
    return mol * 22.4
def litertomol(liter):
    return liter / 22.4
def litertogram(liter, amu):
    return litertomol(liter) * amu
def gramtoliter(gram, amu):
    return moltoliter(gramtomol(gram, amu))
def litertoatom(liter):
    return moltoatom(litertomol(liter))
def atomtoliter(atom):
    return moltoliter(atomtomol(atom))

print("Enter 1 for mole to atom\nEnter 2 for atom to mole\nEnter 3 for atom to gram\nEnter 4 for gram to atom\nEnter 5 for gram to mole\nEnter 6 for mole to gram")
print("Enter 7 for mole to liter\nEnter 8 for liter to mole\nEnter 9 for liter to gram\nEnter 10 for gram to liter")
print("Enter 11 for liter to atom\nEnter 12 for atom to liter")
choice = int(input("Enter your choice: "))
while (choice < 1 or choice > 12):
    print("Invalid choice")
    choice = int(input("Enter your choice: "))
if choice == 1:
    mol = float(input("Enter num. of moles: "))
    answer = moltoatom(mol)
    mol = "{:.6e}".format(answer)
    print("Num of particles is: ", mol)
elif choice == 2:
    par = float(input("Enter num. of particles: "))
    answer = atomtomol(par)
    mol = "{:.6e}".format(answer)
    print("Num of moles is: ", mol)
elif choice == 3:
    atom = float(input("Enter num. of atoms: "))
    atm = float(input("Enter atomic mass: "))
    answer = atomtogram(atom, atm)
    gram = "{:.6e}".format(answer)
    print("Num of grams is: ", gram)
elif choice == 4:
    gram = float(input("Enter num. of grams: "))
    atm = float(input("Enter atomic mass: "))
    answer = gramtoatom(gram, atm)
    atom = "{:.6e}".format(answer)
    print("Num of atoms is: ", atom)
elif choice == 5:
    gram = float(input("Enter num. of grams: "))
    atm = float(input("Enter atomic mass: "))
    answer = gramtomol(gram, atm)
    mol = "{:.6e}".format(answer)
    print("Num of moles is: ", mol)
elif choice == 6:
    mol = float(input("Enter num. of moles: "))
    gram = float(input("Enter atomic mass: "))
    answer = moltogram(mol, gram)
    gram = "{:.6e}".format(answer)
    print("Num of grams is: ", gram)
elif choice == 7:
    mol = float(input("Enter num. of moles: "))
    answer = moltoliter(mol)
    liter = "{:.6e}".format(answer)
    print("Num of liters is: ", liter)
elif choice == 8:
    liter = float(input("Enter num. of liters: "))
    answer = litertomol(liter)
    mol = "{:.6e}".format(answer)
    print("Num of moles is: ", mol)
elif choice == 9:
    liter = float(input("Enter num. of liters: "))
    amu = float(input("Enter atomic mass: "))
    answer = litertogram(liter, amu)
    gram = "{:.6e}".format(answer)
    print("Num of grams is: ", gram)
elif choice == 10:
    gram = float(input("Enter num. of grams: "))
    amu = float(input("Enter atomic mass: "))
    answer = gramtoliter(gram, amu)
    liter = "{:.6e}".format(answer)
    print("Num of liters is: ", liter)
elif choice == 11:
    liter = float(input("Enter num. of liters: "))
    answer = litertoatom(liter)
    atom = "{:.6e}".format(answer)
    print("Num of atoms is: ", atom)
elif choice == 12:
    atom = float(input("Enter num. of atoms: "))
    answer = atomtoliter(atom)
    liter = "{:.6e}".format(answer)
    print("Num of liters is: ", liter)
