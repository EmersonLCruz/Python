# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('gordo','bola','alarme','frigideira','borracha','aristocrata','enfermagem','comida')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ',end='')
    for letras in palavra:
        if letras in 'aeiou':
            print(f'{letras}',end=' ')