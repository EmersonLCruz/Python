# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
cateto_adjacente = float(input('Digite o valor do cateto adjacente:'))
cateto_oposto = float(input('Digite o valor do cateto oposto:'))
#hipotenusa = (cateto_adjacente**2 + cateto_oposto**2)**(1/2)
# math.hypot função de math para calculo da hipotenusa
hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)
print('O valor da Hipotenusa é {:.2f}'.format(hipotenusa))