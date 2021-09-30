cores = {'branco':'\033[m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'cinza':'\033[37m'}

T = 1
M = 5
C = 10

for T in range (M):
    C = C * (1 + T)
        
print(C)
