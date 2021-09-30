soma = 0
for x in range(1,7):
    valor = int(input('Digite um valor:'))
    if valor % 2 == 0:
        soma += x
print('A soma dos valores pares digitados é {}'.format(soma))