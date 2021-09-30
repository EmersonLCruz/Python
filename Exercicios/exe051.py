print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
inicio = int(input('Digite 1º termo da PA:'))
progressao = int(input('Digite valor da progressão:'))
termo = inicio
for x in range (0,10):
    print('{} ->'.format(termo),end=' ')
    termo += progressao
print('ACABOU')