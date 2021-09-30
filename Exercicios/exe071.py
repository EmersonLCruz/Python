'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
valor = int(input('Digite valor do saque: R$ '))
cinquenta = int(valor / 50)
total = int(valor % 50)
vinte = int(total / 20)
total = int(total % 20)
dez = int(total / 10)
total = int(total % 10)


print(f'notas de R$ 50,00 = {cinquenta}')
print(f'Notas de R$ 20,00 = {vinte}')
print(f'Notas de R$ 10,00 = {dez}')
print(f'Notas de R$ 1,00 = {total}')