# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0,10)
print('Pensei em um número entre 0 - 10 você consegue descobrir qual foi?')
jogador = int(input('Digite sua opnião:'))
tentativa = 1
while jogador != computador:
    print('Você errou, tente novamente.')
    if jogador < computador:
        print('O valor que pensei é maior.')
    else:
        print('O valor que pensei é menor.')
    jogador = int(input('Digite sua opnião:'))
    tentativa += 1
print('PARABENS! Você acertou com {} tentativa(s).'.format(tentativa))