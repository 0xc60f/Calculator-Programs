#make a program that takes in the number of electrons and prints out the elctron configuration
elem = int(input("Enter the number of electrons: "))
elecconfig = ""
prefix = ["1s","2s","2p","3s","3p","4s","3d","4p","5s","4d","5p","6s","4f","5d","6p","7s","5f","6d","7p"]
def maxocc (s):
    global maxoccu
    if s[1] == "s":
        maxoccu = 2
    elif s[1] == "p":
        maxoccu = 6
    elif s[1] == "d":
        maxoccu = 10
    elif s[1] == "f":
        maxoccu = 14
for x in range(len(prefix)):
    maxocc(prefix[x])
    if elem == 0:
        break
    elif elem >= maxoccu:
        elecconfig = elecconfig + prefix[x] + str(maxoccu) + " "
        elem = elem - maxoccu
    elif elem < maxoccu:
        elecconfig = elecconfig + prefix[x] + str(elem)
        break
print(elecconfig)
