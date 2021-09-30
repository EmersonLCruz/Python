# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for x in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa:'.format(x)))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('o maior peso é {:.1f} KG'.format(maior))
print('O menor peso é {:.1f} KG'.format(menor))