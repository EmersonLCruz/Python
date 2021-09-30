'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''
valor = (int(input('Digite 1º Valor: ')),int(input('Digite 2º Valor: ')),int(input('Digite 3º Valor: ')),int(input('Digite 4º Valor: ')))
print(f'O número 9 apareceu {valor.count(9)} vezes')
if 3 in valor:
    print(f'O primeiro número 3 aparece na {valor.index(3)+1}º posição')
else:
    print('Não foi difgitado o número 3')
print('Números par digitados: ',end='')
for x in range(0,4):
    if valor[x] % 2 == 0:
        print(valor[x],end=' ')
print('')