from cores import cores
n1 = int(input('Digite primeiro valor:'))
n2 = int(input('Digite segundo valor:'))
if n1 > n2:
    print('Maior valor é:{}'.format(n1))
    print('Menor valor é:{}'.format(n2))
    print('{}O PRIMEIRO VALOR É MAIOR'.format(cores['amarelo']))
elif n1 < n2:
    print('Maior valor é{}'.format(n2))
    print('Menor valor é:{}'.format(n1))
    print('{}O SEGUNDO VALOR É MAIOR'.format(cores['verde']))
else:
    print('Não existe valor maior, os dois são iguais.')