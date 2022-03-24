# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))
imc = peso / (altura ** 2)
print('IMC = {:.2F}'.format(imc))
if imc < 18.5:
    print('Classificação: MAGREZA')
elif  imc <= 24.9:
    print('Classificação: NORMAL')
elif  imc <= 29.9:
    print('Classificação: SOBREPESO')
elif  imc <= 39.9:
    print('Classificação: OBESIDADE')
else:
    print('Classificação: OBESIDADE GRAVE')