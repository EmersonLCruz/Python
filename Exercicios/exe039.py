from datetime import date
from datetime import date
nascimento = int(input('Digite o ano de nascimento:'))
data = date.today().year
alistamento = data - nascimento
#print(alistamento)
if alistamento < 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,alistamento,data))
    print('Ainda faltam {} anos para o alistamento'.format(18 - alistamento))
    print('Seu alistamento será em {}'.format(data + (18 - alistamento)))
elif alistamento > 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,alistamento,data))
    print('Você já deveria ter se alistado há {} anos'.format(alistamento - 18))
    print('Seu alistamento foi em {}'.format(data - (alistamento - 18)))
else:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,alistamento,data))
    print('Você tem que se alistar IMEDIATAMENTE!')
#print(type(data))