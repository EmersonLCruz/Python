# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
for x in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {x}: ')))
print('-='*30)
print(f'Os valores digitados foram: {valores}')
print(f'O maior número digitado foi {max(valores)}, nas posições ',end='')
for x,y in enumerate(valores):
    if y == max(valores):
        print(x,end='... ')
print('')
print(f'O menor valor digitado foi {min(valores)}, nas posições ',end='')
for indice,valor in enumerate(valores):
    if valor == min(valores):
        print(indice,end='... ')