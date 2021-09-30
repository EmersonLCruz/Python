#  Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
jogador['Nome'] = input('Digite o nome do Jogador: ').strip()
partidas = int(input('Quantas partidas ele jogou? '))
jogador['gols'] = []
for x in range(0,partidas):
    gol = int(input(f'Quantos gols na {x+1}º partida:'))
    jogador['gols'].append(gol)
jogador['Total'] = sum(jogador['gols'])
print('='*60)
print(jogador)
print('='*60)
for i,v in jogador.items():
    print(f' - No campo {i} tem o valor {v}')
print('='*60)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for i,p in enumerate(jogador['gols']):
    print(f' - Na partida {i+1}, fez {p} gols')   
print(f'Foi um total de {jogador["Total"]} gols') 