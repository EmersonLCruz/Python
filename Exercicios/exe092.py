# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
cadastro = dict()
cadastro['Nome'] = input('Nome: ').strip()
cadastro['Nascimento'] = int(input('Ano de Nascimento: '))
cadastro['Idade'] = date.today().year - cadastro['Nascimento']
cadastro['CTPS'] = int(input('CTPS: '))
#print(cadastro)
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salario'] = float(input('Salario: R$'))
    cadastro['Aposentadoria'] = cadastro['Contratação'] + 35 - cadastro['Nascimento']
for i,v in cadastro.items():
    print(f'- {i} = {v}')
