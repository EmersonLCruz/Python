nome = input('Digite seu nome completo:').strip()
nome_dividido = nome.split()
print('Seu primeiro nome é {} e seu ultimo nome é {}'.format(nome_dividido[0],nome_dividido[len(nome_dividido) -1]))