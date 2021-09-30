# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = []
valor = 0
for c in range(1,4):
    for x in range(1,4):
        valor = int(input(f'Digite valor [{c},{x}]: '))
        matriz.append(valor)
for c in range(0,9):
    if c == 3 or c == 6:
        print('')
    print(f'[{matriz[c]}]',end='')