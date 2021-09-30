from cores import cores
numero = int(input('Digite um número interio:'))
print("""Escolha uma das bases para conversão
[1] converte para BINÁRIO
[2] converte para OCTAL
[3] converte para HEXADECIMAL""")
opcao = int(input('Sua opção:'))
if opcao == 1:
    binario = bin(numero)
    print('O número {} equivale a {} em binário'.format(numero,binario.lstrip('-0b')))
elif opcao == 2:
    octa = oct(numero)
    print('O número {} equivale a {} em octadecimal'.format(numero,octa.lstrip('0o')))
else:
    hexa = hex(numero)
    print('O número {} equivale a {} em hexadecimal'.format(numero,hexa.lstrip('0x')))
#print('O número {} equivale a {} em binário'.format(numero,binario.lstrip('-0b')))
#print('Binário:{} {}{}'.format(cores['amarelo'],binario.lstrip('-0b'),cores['branco']))
#print('Octadecimal: {}{}{}'.format(cores['verde'],octa.lstrip('0o'),cores['branco']))
#print('Hexadecimal: {}{}{}'.format(cores['vermelho'],hexa.lstrip('0x'),cores['branco']))