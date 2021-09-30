# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
import cores
ano_atual = date.today().year
maiores = 0
menores = 0
for x in range(1,8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(x)))
    idade = ano_atual -nascimento
    if idade >= 18:
        maiores += 1
        #print('{}{}{}'.format(cores.cores['vermelho'],idade,cores.cores['branco']))
    else:
        menores += 1
        #print('{}{}{}'.format(cores.cores['azul'],idade,cores.cores['branco']))
print('Pessoas que atingiram maioridade = {}'.format(maiores))
print('Pessoas que ainda não atingiram maior idade = {}'.format(menores))