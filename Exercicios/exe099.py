# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
from exe097 import linha_adaptavel
def maior(*num):
    maior = num
    linha_adaptavel('Analisando os valores passados')
    if maior == ():
        print('Nenhum valor informado.')
    else:
        for n in maior:
            print(n,end=' ',flush=True)
            sleep(0.5)
        print(f'Foram informados {len(maior)} números')
        print(f'O maior valor é {max(maior)}')



maior()