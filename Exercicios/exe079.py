# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numero = []
while True:
    valor = int(input('Digite um valor: '))
    #print(f'Valor digitado foi {valor}')
    if valor not in numero:
        numero.append(valor)
    else:
        print('Valor duplicado')
    '''if numero == []:
        numero.append(valor)
    else:
        for item in numero:
            if valor in numero:
                print(f'O número {valor} já foi digitado, será descartado.')
                break
            else:
                print('Valor inédito, será acrescentado.')
                numero.append(valor)
                break'''
    opcao = input('Deseja digitar outro número [S/N]? ')
    if opcao[0] in 'Nn':
        break
print(f'os valores digitados sem as repetições foram {numero}')
print(f'Lista ordenada{sorted(numero)}')