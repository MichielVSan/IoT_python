# import the randint function from the module random:
from random import randint
puntentelling = 0
right_answers = 0
try:
    while True:
        n1 = randint(2, 10)
        n2 = randint(2, 10)
        puntentelling +=1
        print('Wat is het product van volgende getallen?\n', n1, n2)
        try:
            answer = int(input('product: '))
        except ValueError:
            print('Ongeldig getal')
            exit()
        product = n1 * n2

        if answer == product:
            print('Gefeliciteerd!')
            right_answers+=1
        else:
            print('Het juiste antwoord was', product)
        if puntentelling==10:
            print(right_answers, "/10")
            break

except KeyboardInterrupt:
    print("tot de volgende")