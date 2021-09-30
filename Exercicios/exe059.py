'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
n1 = int(input('Digite 1º Valor:'))
n2 = int(input('Digite 2º Valor:'))
opcao = 0
while opcao != 5:
    print('''O que deseja executar:
    [1] SOMA
    [2] MULTIPLICAÇÃO
    [3] MAIOR
    [4] NOVOS VALORES
    [5] FINALIZAR EXECUÇÃO''')
    opcao = int(input('Digite sua opção:'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1,n2,soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação de {} x {} = {}'.format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Você digitou {} e {}, o maior valor entre eles é {}'.format(n1,n2,maior))
        else:
            maior = n2
            print('Você digitou {} e {}, o maior valor entre eles é {}'.format(n1,n2,maior))
    elif opcao == 4:
        n1 = int(input('Digite 1º Valor:'))
        n2 = int(input('Digite 2º Valor:'))
    elif opcao > 5:
        print('Opção INVALIDA!')
print('Fim da execução!')
