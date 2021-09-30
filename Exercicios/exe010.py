# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
valor = float(input('Quantos Reais vc tem na carteira? R$'))
print('Com R${} você podde comprar US${:.2f}'.format(valor,valor/3.27))