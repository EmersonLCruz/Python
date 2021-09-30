'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
cont = 0
valores = []
while True:
    valores.append(int(input('Digite valor: ')))
    opcao = input('Deseja digitar outro número [S/N]? ')[0]
    if opcao in 'Nn':
        break
print(f'Os valores digitados foram {valores}')
print(f'A quantidade de valores digitados = {len(valores)}')
valores.sort() # pode usar o comando valores.sort(reverse=True)
print(f'Lista ordenada de forma decrescente: {valores[-1::-1]}')
if 5 in valores:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 NÃO foi digitado.')