salario = float(input('Digite valor do salario: R$'))
if salario <= 1250:
    ajuste_salario = salario + (salario * 0.15)
else:
    ajuste_salario = salario + (salario * 0.1)
print('Salario ajustado para R${:.2f}'.format(ajuste_salario))