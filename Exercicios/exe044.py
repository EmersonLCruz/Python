print('='*10+'SIMULADOR DE COMPRAS'+'='*10)
preco = float(input('Digite valor da compras: R$'))
print("""Escolhaa forma de pagamento
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou + no cartão""")
opcao = int(input('Digite sua opção:'))
if opcao == 1:
    desconto = preco - (preco *0.1)
    print('Sua compra de R${:.2f}, vai custar R${:.2f}.'.format(preco,desconto))
elif opcao == 2:
    desconto = preco - (preco * 0.05)
    print('Sua compra de R${:.2f}, vai custar R${:.2f}'.format(preco,preco - (preco * 0.05)))
elif opcao == 3:
    print('Sua compra de R${:.2f}, parcelado em 2x de R${:.2f}'.format(preco,preco / 2))
else:
    parcela = int(input('Quantidade de parcelas entre (3 - 12):'))
    juros = preco + (preco * 0.2)
    print('Sua compra de R${:.2f}, vai custar R${:.2f}, em {} parcelas de R${:.2f}'.format(preco,juros,parcela,juros / parcela))
