
#SCIENTIFIC CALCULATOR#
print("WELCOME TO THE SCIENTIFIC CALCULATOR")
print("|______________________________________________|")
print("| ON |   | OFF |    |CHECK|     | -->|    |<-- |")
print("|sin |  | cos |  | tan |  | pow|  | ac  |  |DEL|")
print("| 7  |  |  8  |  |  9  |  | deg|  | rad |  |M +|")
print("| 4  |  |  5  |  |  6  |  |mod |  |sqrt |  |M -|")
print("| 1  |  |  2  |  |  3  |  |  / |  |  *  |  |M =|")
print("| 00 |  |  0  |  |  .  |  |  + |  |  -  |  | = |")

#BEGINING OF CODE

import math
def add(a,b):
    return a+b
def subtract(c,d):
    return c-d
def multiply(e,f):
    return e*f
def divide(g,h):
    return g/h
def mod (i,j):
    return i%j
def root(k):
    return math.sqrt(k)
def power (l,m):
    return pow(l,m)
def sin(n):
    return math.sin(n)
def cos(o):
    return math.cos(o)
def tan(p):
    return math.tan(p)
def deg(q):
    return math.degrees(q)
def rad(r):
    return math.radians(r)

#USER INPUT

#CALLING OF FUNCTION 

# PRINTING OF OUTPUT


while True:
    ch=input("OPERATION: ")
    if ch in  ( '+', '-' , '*' , '/' , 'pow' , 'mod' , 'sqrt','sin' , 'cos' , 'tan' , 'deg' , 'rad'):
        if ch=='+':
             n1=float(input("ENTER NUMBER:"))
             n2=float(input("ENTER NUMBER:"))
             print(add(n1,n2))
        elif ch=='-':
             n1=float(input("ENTER NUMBER:"))
             n2=float(input("ENTER NUMBER:"))
             print(subtract(n1,n2))
        elif ch=='*' :
             n1=float(input("ENTER NUMBER:"))
             n2=float(input("ENTER NUMBER:"))
             print(multiply(n1,n2))
        elif ch=='/' :
             n1=float(input("ENTER NUMBER:"))
             n2=float(input("ENTER NUMBER:"))
             print(divide(n1,n2))
        elif ch=='pow':
            n1=float(input("ENTER NUMBER:"))
            n2=float(input("ENTER NUMBER:"))
            print(pow(n1,n2))
        elif ch=='mod':
            n1=float(input("ENTER NUMBER:"))
            n2=float(input("ENTER NUMBER:"))
            print (mod(n1,n2))
        elif ch=='sqrt':
            n1=float(input("ENTER NUMBER:"))
            print(root(n1))
        elif ch=='sin':
             n1=float(input("ENTER NUMBER:"))
             print(sin(n1))
        elif ch=='cos':
             n1=float(input("ENTER NUMBER:"))
             print(cos(n1))
        elif ch=='tan':
             n1=float(input("ENTER NUMBER:"))
             print(tan (n1))
        elif ch=='deg':
             n1=float(input("ENTER NUMBER:"))
             print(deg(n1))
        elif ch=='rad':
             n1=float(input("ENTER NUMBER:"))
             print(rad(n1))

 # BREAKING OF LOOP 
 
        next_calculation = input("Let's do next calculation? (yes/no): ")      
        if next_calculation == "no":
          break
    
    else:
        print("! ! INVALID ! !")
          
# CODE GETS END 
