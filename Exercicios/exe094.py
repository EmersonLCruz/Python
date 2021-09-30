# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
cadastro = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa['Nome'] = input('Nome: ')
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        pessoa['Sexo'] = input('Sexo [F/M]: ').strip().upper()[0]
        if pessoa['Sexo'] not in 'FM':
            print('Valor invalido por favor digite F ou M.')
        else:
            break
    cadastro.append(pessoa.copy())
    while True:
        sair = input('Deseja Sair? [S/N]: ').strip().upper()[0]
        if sair not in 'SN':
            print('Valor invalido por favor digite S ou N.')
        else:
            break
    if sair in 'Ss':
        break
print(cadastro)
print(f'A) Foram cadastradas {len(cadastro)} pessoas.')
for p in cadastro:
    soma += p['Idade']
    media = soma / len(cadastro)
print(f'B) A média de idade das pesoas cadastras é de {media:.1f} anos.')
print('C) Lista das Mulheres Cadastradas:')
for p in cadastro:
    if p['Sexo'] == 'F':
        print(f'=> {p["Nome"]} com {p["Idade"]} anos.')
print('D) Lista de Pessoas com idade acima da média:')
for p in cadastro:
    if p['Idade'] > media:
        print(f'=> {p["Nome"]} com {p["Idade"]} anos.')