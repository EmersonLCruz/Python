# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
valores = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print('Os números sorteados foram: ',end=' ')
for item in valores:
    print(f'{item}', end=' ')
'''maior = menor = 0
lista = []
for x in range(0,5):
    lista.append(randint(0,100))
valor = tuple(lista)
print(valor)
for x in range(0,5):
    if maior == 0 and menor == 0:
        maior = menor = valor[x]
    else:
        if maior < valor[x]:
            maior = valor[x]
        elif menor > valor[x]:
            menor = valor[x]'''
print('')
print(f'O maior valor é {max(valores)} e o menor valor é {min(valores)}')
