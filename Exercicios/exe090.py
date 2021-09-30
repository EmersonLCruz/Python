# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['Nome'] = input('Nome do aluno(a): ')
aluno['Média'] = float(input(f'Média do aluno {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 3 <= aluno['Média'] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('='*30)
print(f'Nome: {aluno["Nome"]}')
print(f'Média: {aluno["Média"]}')
print(f'Situação: {aluno["Situação"]}')