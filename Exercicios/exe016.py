# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

n = float(input('Digite um valor real:'))
print('O valor digitado foi {} e sua porção inteira é {}.' .format(n,math.trunc(n)))