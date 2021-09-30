from datetime import date
nascimento = int(input('Ano de nascimento:'))
data_atual = date.today().year
idade = data_atual - nascimento
print('A idade do atleta é {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL') 
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
