# Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Digite um valor:'))
cont = 2
fatorial = 1
while cont < n+1 :
    fatorial = fatorial * cont
    cont += 1
print('O fatorial de {} é {}'.format(n,fatorial))