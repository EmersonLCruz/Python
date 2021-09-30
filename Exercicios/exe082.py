# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = list()
while True:
    valores.append(int(input('Digite valor: ')))
    opcao = input('Deseja digitar outro número [S/N]? ')[0]
    if opcao in 'Nn':
        break
pares = list()
impares = []
for indice,numeros in enumerate(valores):
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(valores[indice])
print('='*30)
print(f'Você digitou {valores}')
print(f'Os valores pares contidos na lista: {sorted(pares)}')
print(f'Os valores impares contidos na lista: {sorted(impares)}')