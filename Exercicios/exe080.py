# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []

for x in range(0,5):
    valor = int(input('Digite valor: '))
    # verifica se a lista esta vazia ou se o valor maior que o ultimo elemento
    if x == 0 or valor > numeros[-1]:
        numeros.append(valor)
        print('Valor inserido ao final da lista...')
    else:
        # Varre a lista, enquanto o valor maior, se valor menor igual acrescentar na posição de aux 
        aux = 0
        while aux < len(numeros):
            if valor <= numeros[aux]:
                numeros.insert(aux, valor)
                print(f'Valor inserido na posição {aux} da lista...')
                break
            aux += 1
print('='*30)
print(f'Os valores ordenados são {numeros}')
'''for x in range(0,5):
    for y in range(x+1,5):
        
        if numeros[x] > numeros[y]:
            aux = numeros[x]
            numeros[x] = numeros[y]
            numeros[y] = aux'''

        