# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termo = int(input('Digite quantos termos da sequência quer mostrar: '))
cont = 0
fibo1 = 0
fibo2 = 1
while cont != termo:
    if cont == 0:
        print('{}'.format(fibo1),end='-')
        cont += 1
    elif cont == 1:
        print('{}'.format(fibo2),end='-')
        cont += 1
    else:
        fibonacci = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibonacci
        print('{}'.format(fibonacci),end='-')
        cont += 1
print('FIM')