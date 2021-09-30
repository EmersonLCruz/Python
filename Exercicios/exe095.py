# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
gol_partida = []
cadastro = []
while True:
	jogador['Nome'] = input('Digite o nome do Jogador: ').strip()
	partidas = int(input('Quantas partidas ele jogou? '))
	for x in range(0,partidas):
		gol = int(input(f'Quantos gols na {x+1}º partida:'))
		gol_partida.append(gol)
	jogador['gols'] = gol_partida[:]
	jogador['Total'] = sum(jogador['gols'])
	cadastro.append(jogador.copy())
	gol_partida.clear()
	sair = input('Deseja Sair? [S/N]: ')
	if sair in 'Ss':
		break
print('='*60)
print(cadastro)
print('='*60)
print(f'{"Cod":<5}{"Jogador":<10}{"Total Gols"}')
for i,v in enumerate(cadastro):
	print(f'{i:<5}{v["Nome"]:<10}{v["Total"]}')
print('='*60)
while True:
	opcao = int(input('Digite Codigo do jogador ou 999 para sair: '))
	if opcao == 999:
		break
	if opcao >= len(cadastro):
		print('Valor Invalido, Digite Codigo do jogador ou 999 para sair: ')
	else:
		print(f' - Levantamento do Jogador {cadastro[opcao]["Nome"]}')
		for i,p in enumerate(cadastro[opcao]['gols']):
			print(f'Na partida {i+1} fez {p} gols')
	print('='*60)

