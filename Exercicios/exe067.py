# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    print('='*30)
    tabuada = 'TABUADA'
    print(f'{tabuada:^30}')
    print('='*30)
    n = int(input('Digite um número: '))
    if n < 0:
        break
    else:
        for x in range(1,11):
            print(f'{n:} x {x:2} = {n*x}')