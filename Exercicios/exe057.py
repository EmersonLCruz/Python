# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = 'a'
while sexo not in 'MF':
    sexo = input('Digite sexo [M/F]:').upper().strip()[0]
    if sexo not in 'MF':
        print('Valor invalido!')