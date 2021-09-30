# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o valor do angulo:'))
coseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Coseno de {} é {:.2f}'.format(angulo,coseno))
print('Seno de {} é {:.2f}'.format(angulo,seno))
print('Tangente de {} é {:.2f}'.format(angulo,tangente))