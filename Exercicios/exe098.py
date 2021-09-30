# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada
from time import sleep
from exe097 import linha_adaptavel


def contador():
    for x in range(1,11):
        print(x, end=' ', flush=True)
        sleep(0.5)
    print('')
    for x in range(10,-1,-2):
        print(x, end=' ', flush=True)
        sleep(0.5)
    print('')
    linha_adaptavel('Vamos personalizar?')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo < 0:
        passo *= -1
    print(f'Iniciando a contagem de {inicio} ate {fim} salteando de {passo}')
    if inicio > fim:
        for x in range(inicio,fim,passo * -1):
            print(x, end=' ', flush=True)
            sleep(0.5)
    else:
        for x in range(inicio,fim,passo):
            print(x,end=' ', flush=True)
            sleep(0.5)
    


contador()