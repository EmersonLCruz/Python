'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
maior_18 = menor_20 = homen = 0
while True:
    print('Cadastro de Pessoas')
    print('-'*30)
    idade = int(input('Entre com valor da idade: '))
    sexo = input('Entre com o sexo [M/F]: ').strip().upper()[0]
    if idade >= 18:
        maior_18 += 1
    if sexo == 'F' and idade < 20:
        menor_20 += 1
    if sexo == 'M':
        homen += 1
    opcao = input('Deseja cadastrar outra pessoa? [S/N]: ').strip().upper()[0]
    if opcao == 'N':
        break
print('='*30)
relatorio = 'RELATÓRIO'
print(f'{relatorio:^30}')
print('='*30)
print(f'Foram cadastradas {maior_18} pessoas com idade superior a 18.')
print(f'Foram cadastrados {homen} homem(s).')
print(f'Foram cadastrados {menor_20} de mulheres com idade inferior a 20.')