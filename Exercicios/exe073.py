'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''
times = ('Atlético-MG','Palmeiras','Fortaleza','Bragantino','Flamengo','Atlético-GO','Athletico-PR','Ceará SC','Internacional','Santos','Corinthians','Juventude','Bahia','São Paulo','Fluminense','Cuiabá','Sport Recife','América-MG','Grêmio','Chapecoense')
print('='*30)
print(f'Lista do Brasileirão 2021: {times}')
print('='*30)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('='*30)
print(f'Os ultimos 4 colocados são: {times[16:]}')
print('='*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('='*30)
print(f'O Chapecoense esta {times.index("Chapecoense")+1}º posição')
print('='*30)