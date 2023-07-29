import math

def heron(a,b,c,s):
  deez = s*(s-a)*(s-b)*(s-c)
  deez = pow(deez,0.5)
  return deez 

a=float(input("Enter side 1: "))
b=float(input("Enter side 2: "))
c=float(input("Enter side 3: "))

sthis = float((a+b+c)/2)
area = heron(a,b,c,sthis)
answer = "{:.6e}".format(area)
print(answer)
  
  
 