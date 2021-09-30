# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
primeiro_termo = int(input('Digite valor do 1º termo: '))
razao = int(input('Digite a razão: '))
cont = 0
aux = 11
pa = primeiro_termo
while cont != aux:
    print('{} ->'.format(pa),end=' ')
    pa += razao
    cont += 1
    if cont == aux-1:
        print('PAUSA')
        novo_termo = int(input('Deseja mostrar mais quantos termos? '))
        if novo_termo > 0:
            aux += novo_termo
        else:
            aux -= 1
print('Progressão finalizada com {} termos mostrados'.format(cont))

