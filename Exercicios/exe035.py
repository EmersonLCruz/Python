a = int(input('Digite valor da primeira reta:'))
b = int(input('Digite valor da segunda reta:'))
c = int(input('Digite valor da terceira reta:'))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Os segmentos {}, {} e {} podem formar um triangulo.'.format(a,b,c))
else:
    print('Os segmentos {}, {} e {} não podem formar um triangulo.'.format(a,b,c))