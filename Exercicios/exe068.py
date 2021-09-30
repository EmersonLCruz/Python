# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = True
cont = 0
while vitoria != False:
    computador = randint(0,10)
    jogador = int(input('Digite um número: '))
    opcao = input('Digite sua opção [P] Par [I] Impar: ').strip().upper()[0]
    soma = jogador + computador
    print(f'Você colocou {jogador} e o computador {computador}, resultado {soma}')
    if soma % 2 == 0 and opcao == 'P' or soma % 2 and opcao == 'I':
        if soma % 2 == 0:
            print(f'{soma} é PAR')
        else:
            print(f'{soma} é IMPAR')
        print('Jogador VENCEU!')
        cont += 1
    else:
        if soma % 2 == 0:
            print(f'{soma} é PAR')
        else:
            print(f'{soma} é IMPAR')
            print('Computador VENCEU!')
        break
print('-'*30)
print('FIM do JOGO!')
print(f'Você venceu {cont} vezes')