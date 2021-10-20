from random import randint
n = randint(0,100)
getal = int(input("geef een getal: "))
aantal_gokken=0
while getal!=n:
    if getal>n:
        print("lager!")
        
    else:
        print("hoger!")
    aantal_gokken+=1
    getal = int(input("geef een getal: "))
print("u heeft het geraden in", aantal_gokken, "keer.")