'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna. 
C) O maior valor da segunda linha.'''
matriz = []
valor = soma_par = soma = 0

for x in range(1,4):
    for y in range(1,4):
        valor = int(input(f'Digite valor na posição [{x},{y}]: '))
        matriz.append(valor)
print('-='*15)
print(f'{"VALORES DIGITADOS"}')
for x in range(0,9):
    if x == 3 or x == 6:
        print('')
    print(f'[{matriz[x]:^5}]',end='')
    if matriz[x] % 2 == 0:
        soma_par += matriz[x]
    if x == 2 or x == 5 or x == 8:
        soma += matriz[x]
print('')
print('-='*15)
print(f'A soma dos números pares digitados é: {soma_par}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {max(matriz[3:6])}')
