'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
total = cont = valor_barato = 0
while True:
    produto = input('Entre com o nome do produto: ').strip()
    valor = float(input('Digite o valor: R$ '))
    total += valor
    if valor_barato == 0:
        produto_barato = produto
        valor_barato = valor
    elif valor < valor_barato:
        produto_barato = produto
        valor_barato = valor
    if valor >= 1000:
        cont += 1
    opcao = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if opcao != 'S':
        break
print('-'*30)
print(f'O total gasto nas compras é R$ {total}')
print(f'Existe na sacola {cont} itens com valor superior a R$ 1000,00')
print(f'O produto mais barato é {produto_barato} que custa R$ {valor_barato:.2f}')