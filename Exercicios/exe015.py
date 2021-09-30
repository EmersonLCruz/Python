# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input('Digite quantidades de dias que o carro foi locado:'))
km = float(input('Digite quantos kilometros foram rodados:'))
pagar = (60 * dia) + (0.15 * km)
print('Valor cobrado por dia é R$60.00, logo {} dias = R${:.2f}'.format(dia,dia*60))
print('Valor cobrado por Kilometros rodados é R$0.15, logo {} km = R${:.2f}'.format(km,km*0.15))
print('Total = R${:.2f}'.format(pagar))