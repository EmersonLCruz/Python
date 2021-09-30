nota1 = float(input('Digite primeira nota:'))
nota2 = float(input('Digite segunda nota:'))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('Tirando {} e {}, a média é {}'.format(nota1,nota2,media))
    print('O aluno está APROVADO!')
elif media >= 5.0:
    print('Tirando {} e {}, a média é {}'.format(nota1,nota2,media))
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('Tirando {} e {}, a média é {}'.format(nota1,nota2,media))
    print('O aluno está REPROVADO!')