distancia = float(input('Qual a distancia a ser percorrida na viagem?'))
if distancia <= 200.0:
    valor = distancia * 0.5
    print('Valor da sua passagem é R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('Valor da sua passagem é R${:.2f}'.format(valor))