# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
valores = [[],[]]
numero = 0
for x in range(0,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero) 
print('='*30)
valores[0].sort() # Ordena de forma permanente
print(f'Os valores pares são {valores[0]}') 
print(f'Os valores impares são {sorted(valores[1])}') # Ordena de forma temporaria mantem lista original
