velocidade = float(input('Computando velocidade:'))
if velocidade > 80.0:
    print("""Sua velocidade atual é {}
    Você excedeu o limite de velocidade de 80km em {}km
    multa de R${:.2f}""".format(velocidade,velocidade - 80,(velocidade - 80)*7))
else:
    print('Sua velocidade é {}km, velocidade permitida 80km'.format(velocidade))