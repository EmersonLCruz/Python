# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('='*30)
print(f'{"PALPITES DA MEGA SENA":^30}')
print('='*30)
aposta = list()
numero = cont = 0
quantidade_jogo = int(input('Digite quantidade de apostas: '))
#print('='*30)
for j in range(0,quantidade_jogo):
    aposta.append([])
for j in range (0,len(aposta)):
    cont = 0
    while cont < 6:
        numero = randint(1,60)
        if numero not in aposta[j]:
            aposta[j].append(numero)
            cont += 1
    sleep(1)
    print(f'Jogo {j+1}: {aposta[j]}')
  
            

