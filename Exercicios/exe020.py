# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno = []
aluno.append(input('Digite nome do primeiro aluno:'))
aluno.append(input('Digite nome do segundo aluno:'))
aluno.append(input('Digite o nome do terceiro aluno:'))
aluno.append(input('Digite o nome do quarto aluno:'))
#sorteado = random.randint(0,3)
random.shuffle(aluno)
print('Ordem de Apresentação:')
print(aluno)
'''print('Primeiro {}'.format(aluno[sorteado]))
aluno.pop(sorteado)
sorteado = random.randint(0,2)
print('Segundo {}'.format(aluno[sorteado]))
aluno.pop(sorteado)
sorteado = random.randint(0,1)
print('Terceiro {}'.format(aluno[sorteado]))
aluno.pop(sorteado)
print('Quarto {}'.format(aluno[0]))'''