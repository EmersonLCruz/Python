a = int(input('Digite valor da primeira reta:'))
b = int(input('Digite valor da segunda reta:'))
c = int(input('Digite valor da terceira reta:'))
if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b and a == c:
        print('Essas retas formam um triangulo EQUILATERO')
    elif a != b and a != c and b != c:
        print('Essas retas formam um triangulo ESCALENO')
    else:
        print('Essas retas formam um triangulo ISOCELES')
else:
    print('Essas retas NÃO formam um triangulo.')