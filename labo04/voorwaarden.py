getal1 = int(input('geef een getal'))
getal2 = int(input('geef een tweede getal'))
bewerking = input('welke bewerking wil je doet')

if bewerking == '+':
    print('de som van', getal1, 'en', getal2, 'is:', getal1 + getal2 )
elif bewerking == '-':
    print('het verschil van', getal1, 'en', getal2, 'is:', getal1 - getal2 )
else:
    print('bewerking is niet ge\xefmplementeerd')
