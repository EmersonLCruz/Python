from random import randint
from time import sleep
computador = randint(0,2)
jogadas = {0:'PEDRA',1:'TESOURA',2:'PAPEL'}
print('''Suas opções:
[0] PEDRA
[1] TESOURA
[2] PAPEL''')
jogador = int(input('Sua opçao:'))
if jogador > 2:
    print('Opção INVALIDA, Você PERDEU')
    print('COMPUTADOR jogou {}'.format(jogadas[computador]))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if jogador == computador:
    print('JOGADOR = {}'.format(jogadas[jogador]))
    print('COMPUTADOR = {}'.format(jogadas[computador]))
    print('EMPATE')
elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
    print('JOGADOR = {}'.format(jogadas[jogador]))
    print('COMPUTADOR = {}'.format(jogadas[computador]))
    print('JOGADOR VENCEU!')
else:
    print('JOGADOR = {}'.format(jogadas[jogador]))
    print('COMPUTADOR = {}'.format(jogadas[computador]))
    print('COMPUTADOR VENCEU!')