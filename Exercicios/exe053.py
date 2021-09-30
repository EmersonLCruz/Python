# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase:').upper().strip()
frase = frase.split()
frase_junto = ''.join(frase)
frase_inversa = ''
for x in range(len(frase_junto)-1,-1,-1):
    frase_inversa += frase_junto[x]
print('A frase {} invertida é {}'.format(frase_junto,frase_inversa))
if frase_junto == frase_inversa:
    print('Portanto é PALÍNDROMA')
else:
    print('Portanto NÃO é PALÍNDROMA')