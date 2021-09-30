# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite valor da temperatura em Celsius:'))
fahrenheit = 1.8 * celsius + 32
print('{:.1f}ºC = {:.1f}ºF'.format(celsius,fahrenheit))