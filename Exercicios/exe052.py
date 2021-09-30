# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from cores import cores
numero = int(input('Digite um númeor inteiro:'))
cont = 0
for x in range (1,numero + 1):
    if numero % x  == 0:
        print('{}{}{}'.format(cores['amarelo'],x,cores['branco']),end=' ')
        cont += 1
    else:
        print('{}{}{}'.format(cores['vermelho'],x,cores['branco']),end=' ')
print()
if cont == 2:
    print('O número {} foi divisivel {} vezes,portanto ele é PRIMO'.format(numero,cont))
else:
    print('O número {} foi divisivel {} vezes,portanto ele NÃO é PRIMO'.format(numero,cont))