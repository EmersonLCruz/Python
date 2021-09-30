# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite uma distância em metros:'))
print('A medida de {}m correspode a'.format(n))
print('{}km'.format(n/1000))
print('{}hm'.format(n/100))
print('{}dam'.format(n/10))
print('{}dm'.format(int(n*10)))
print('{}cm'.format(int(n*100)))
print('{}mm'.format(int(n*1000)))