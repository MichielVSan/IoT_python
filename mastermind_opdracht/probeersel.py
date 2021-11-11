g1=int(input("gg"))
g2=int(input("gg"))
g3=int(input("gg"))
g4=int(input("gg"))
aantal_gokken=9
n1=6
n2=7
n3=3
n4=5

if g1 == n1:
    print("X")
    n1=10
if g2 == n2:
    print("X")
    n2=10
if g3 == n3:
    print("X")
    n3=10
if g4 == n4:
    print("X")
    n4=10
if n2 == g1 or n3 == g1 or n4 == g1:
    print("x")
if n1 == g2 or n3 == g2 or n4 == g2:
    print("x")
if n1 == g3 or n2 == g3 or n4 == g3:
    print("x")
if n1 == g4 or n2 == g4 or n3 == g4:
    print("x")
if aantal_gokken != 0:
    print("probeer opnieuw!")