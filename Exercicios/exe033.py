n1 = int(input('Digite primeiro número:'))
n2 = int(input('Digite segundo número:'))
n3 = int(input('Digite terceiro número:'))
if n1 > n2 and n1 > n3:
    valor = n1
elif n2 > n1 and n2 > n3:
    valor = n2
else:
    valor = n3
print('O maior número é {}'.format(valor))
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print('O menor número é {}'.format(menor))