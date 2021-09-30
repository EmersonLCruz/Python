# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    msg = ''
    idade = date.today().year - ano
    print(f'Sua idade é de {idade} anos.')
    if (16 <= idade < 18) or idade > 65:
        msg = 'Voto Opcional'
        return msg
    elif 18 <= idade <= 65:
        msg = 'Voto Obrigatorio'
        return msg
    else:
        msg = 'Voto Negado'
        return msg


nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))
#print(msg)
