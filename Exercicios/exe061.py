# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
primeiro_termo = int(input('Digite o 1º termo da PA:'))
razao = int(input('Digite a razão:'))
cont = 0
pa = primeiro_termo
while cont != 10:
    print('{} ->'.format(pa),end=' ')
    pa += razao
    cont += 1
print('ACABOU!')