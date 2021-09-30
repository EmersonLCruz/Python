# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
jogadores = {'j1':randint(1,6),'j2':randint(1,6),'j3':randint(1,6),'j4':randint(1,6)}
aux = 0
print('='*5,'Jogadores Lançam os dados','='*5)
for i,j in enumerate(jogadores):
    print(f'O jogador {i+1} tirou {jogadores[j]}')
print('='*10,'Classificação','='*10)
for i in sorted(jogadores, key = jogadores.get, reverse=True):# ordenar jogadores pela chave em ordem decrescente
    aux += 1
    print(f'{aux}º posição {i} com resultado {jogadores[i]}')
