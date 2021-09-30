'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,mostre:     A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoas = list()
cadastro = list()
peso_total = media_peso =0
while True:
    pessoas.append(input('Digite nome: '))
    pessoas.append(float(input('Digite peso:Kg ')))
    cadastro.append(pessoas[:])
    pessoas.clear()
    opcao = input('Deseja cadastrar outra pessoa [S/N]? ').strip()[0]
    if opcao in 'Nn':
        break
print('='*50)
print(cadastro)
print(f'Foram cadastrados {len(cadastro)} pessoas.')
for p in cadastro:
    peso_total += p[1]
media_peso = peso_total / len(cadastro)
print(f'A média de peso do grupo = {media_peso}Kg')
print('-'*50)
print('PESSOAS COM PESO ACIMA DA MÉDIA'.center(50))
for p in cadastro:
    if p[1] > media_peso:
        print(f'{p[0]} peso de {p[1]}Kg')
print('-'*50)
print('PESSOAS COM PESO ABAIXO DA MÉDIA'.center(50))
for p in cadastro:
    if p[1] < media_peso:
        print(f'{p[0]} peso de {p[1]}Kg')
    