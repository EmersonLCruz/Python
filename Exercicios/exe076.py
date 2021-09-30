# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Borracha',0.5,'Lápis',0.85,'Caderno',15.99,'Caneta',1.5)
print('='*30)
print(f'{"TABELA DE PRODUTOS":^30}')
print('='*30)
for item in range(0,len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<20}',end='')
    else:
        print(f'R${produtos[item]:>7.2f}')