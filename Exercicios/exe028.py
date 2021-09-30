import random
numero = random.randint(0,5)
print('Pensei em um número entre 0 e 5, você consegue descobrir qual foi?')
valor = int(input('Digite o número que você acha que pensei:'))
if valor == numero:
    print('Parabens! Acertou!')
else:
    print('Você errou o número que pensei foi {}'.format(numero))