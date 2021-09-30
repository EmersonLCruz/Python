# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno = []
aluno.append(input('Digite nome do primeiro aluno:'))
aluno.append(input('Digite nome do segundo aluno:'))
aluno.append(input('Digite o nome do terceiro aluno:'))
aluno.append(input('Digite o nome do quarto aluno:'))
print(aluno)
# .choice escolhe um valor randomico dentro de uma lista
#sorteado = random.choice(aluno)
sorteado = random.randint(0,3)
print('O aluno sorteado foi {}'.format(aluno[sorteado]))
aluno.pop(sorteado)
print(aluno)