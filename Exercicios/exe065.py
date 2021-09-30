# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
maior = menor = cont = soma = 0
opcao = 'N'
while opcao != 'S':
    n = int(input('Digite um número interio: '))
    cont += 1
    soma += n
    media = soma / cont
    if maior == 0:
        maior = n
    if menor == 0:
        menor = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    opcao = input('Deseja sair [S/N]: ').strip().upper()[0]
print('Você digitou {} números e a média entre eles é {}'.format(cont,media))
print('O maior número é {}, e o menor é {}'.format(maior,menor))