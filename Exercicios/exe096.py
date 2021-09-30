# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(altura,comprimento):
    dimensao = altura*comprimento
    print(f'A area do terreno {altura}m x {comprimento}m é {dimensao:.2f}m²')


largura = float(input('Digite Largura do terreno (m): '))   
comprimento = float(input('Digite Comprimento do terreno (m): '))
area(largura,comprimento) 
