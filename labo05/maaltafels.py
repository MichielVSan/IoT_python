# import the randint function from the module random:
from random import randint
try:
    while True:
        n1 = randint(2, 10)
        n2 = randint(2, 10)
        print('Wat is het product van volgende getallen?\n', n1, n2)
        try:
            answer = int(input('product: '))
        except ValueError:
            print('Ongeldig getal')
            exit()
        product = n1 * n2

        if answer == product:
            print('Gefeliciteerd!')
        else:
            print('Het juiste antwoord was', product)
except KeyboardInterrupt:
    print("tot de volgende")