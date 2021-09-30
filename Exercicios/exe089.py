# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
aluno = list()
boletim = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = (nota1 + nota2) /2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    opcao = input('Deseja fazer novo cadastro [S/N]: ').strip()[0]
    if opcao in 'Nn':
        break
print('-'*30)
print(f'{"Nº":<4}{"Nome":<15}{"Média":>8}')
for i in range(0,len(boletim)):
    print(f'{i+1:<4}{boletim[i][0]:<15}{boletim[i][3]:>8.1f}')
print('-'*30)
while True:
    sair = int(input('Digite número do aluno ou 9999 para sair: '))
    print('='*30)
    if sair == 9999:
        break
    else:
        print(f'As notas de {boletim[sair-1][0]}')
        print(f'Nota 01: {boletim[sair-1][1]}')
        print(f'Nota 02: {boletim[sair-1][2]}')
        print('='*30)


#print(boletim)