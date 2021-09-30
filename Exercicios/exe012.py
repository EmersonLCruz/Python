# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Qual o valor do produto:R$'))
print('Esse produto que custa R${}, na promoção com desconto de 5% vai custar r${:.2f}.'.format(valor,valor-valor*0.05))