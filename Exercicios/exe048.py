import emoji
cont = 0
valor = 0
for x in range(3,501,3):
    if x % 2 == 1 and x % 3 == 0:
        valor += x
        cont += 1
print(emoji.emojize('A soma de todos os {} valores solicitados é {}:rosto_sorridente_com_óculos_escuros:',language = 'pt').format(cont,valor))