from operator import truediv
import random
moeilijkheidsgraad = input("kies een moeilijkheidgraad.(makkelijk,moeilijk of extreem): ")
aantal_kleuren = 7
possible_colours=['blauw', 'geel', 'groen', 'oranje', 'paars', 'rood', 'wit', 'zwart']
if moeilijkheidsgraad == "makkelijk":
    aantal_gokken=16
    possible_colours.append
elif moeilijkheidsgraad == "moeilijk":
    aantal_gokken=12
elif moeilijkheidsgraad == "extreem":
    aantal_gokken=12
    possible_colours.append("bruin")
    aantal_kleuren+=1
try:
    aantal_gokken*1
except NameError:
    print("u bent de moeilijkheidsgraad vergeten.")
    moeilijkheidsgraad = input("kies een moeilijkheidgraad.(makkelijk,moeilijk of extreem): ")
    if moeilijkheidsgraad == "makkelijk":
        aantal_gokken=16
    elif moeilijkheidsgraad == "moeilijk":
        aantal_gokken=12
    elif moeilijkheidsgraad == "extreem":
        aantal_gokken=12
        possible_colours.append("bruin")
        aantal_kleuren+=1
print("dit zijn de mogelijke kleuren:", possible_colours)
n= random.sample(range(0,aantal_kleuren), 4)
n1=n[0]
n2=n[1]
n3=n[2]
n4=n[3]
colour1 = possible_colours[n1]
colour2 = possible_colours[n2]
colour3 = possible_colours[n3]
colour4 = possible_colours[n4]
g1= 0
g2= 0
g3= 0
g4= 0
while True:
    if aantal_gokken==-1:
        print("game over, de juiste kleuren waren:", colour1, ",", colour2, ",", colour3, ",", colour4)
        exit()
    gok1=input("geef een kleur: ")
    gok2=input("geef een tweede kleur: ")
    gok3=input("geef een derde kleur: ")
    gok4=input("geef een laatste kleur: ")
    try:
        g1=possible_colours.index(gok1)
        g2=possible_colours.index(gok2)
        g3=possible_colours.index(gok3)
        g4=possible_colours.index(gok4)
    except ValueError:
        print("geen kleur uit de lijst gekozen.")
        continue
    aantal_gokken-=1
    if (n1==g1 and n2==g2 and n3==g3 and n4==g4):
        print("u hebt het geraden!!!")
        exit()
    if n1 == g1:
        print("X") 
    if  n2 == g2:
        print("X")
    if n3 == g3:
        print("X")
    if n4 == g4:
        print("X")
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
        print("u hebt nog", aantal_gokken, "kansen")