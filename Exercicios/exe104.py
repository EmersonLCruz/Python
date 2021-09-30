# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    from cores import cores
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            return n
            break
        else:
            print(f'{cores["vermelho"]}Erro! Digite um numero inteiro{cores["branco"]}')
            
            
    
    

valor = leiaInt('Digite um numero: ')
print(f'Você digitou {valor}')