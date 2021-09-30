# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sorteia():
    valores = [randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)]
    print('Sorteando 5 valores: ',end=' ')
    for x in valores:
        print(x,end=' ',flush=True)
        sleep(0.5)
    print('PRONTO')
    return valores


def somaPar(num):
    soma = 0
    for v in num:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos pares é {soma}')




numeros = sorteia()
somaPar(numeros)
