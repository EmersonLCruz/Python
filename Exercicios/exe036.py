from cores import cores

print('-='*20)
print('      {}SIMULADOR DE FINANCIAMENTO{}'.format(cores['amarelo'],cores['branco']))
print('-='*20)
valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
parcela = int(input('Digite em quantos anos deseja financiar:'))* 12
print()
print('valor da parcela = {}R${:.2f}{}'.format(cores['verde'],valor_casa / parcela,cores['branco']))
print('Valor maximo da parcela para aprovação do financiamento = {}R${:.2f}{}'.format(cores['amarelo'],salario * 0.3,cores['branco']))
if (valor_casa / parcela) > (salario * 0.3):
    print('Financiamento {}NEGADO{}, parcelas não pode exceder 30% do salário'.format(cores['vermelho'],cores['branco']))
print('Financiamento {}APROVADO!{}'.format(cores['amarelo'],cores['branco']))