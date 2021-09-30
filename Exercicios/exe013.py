# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o seu salario: R$'))
salario_ajustado = salario + (salario*15/100)
print('Seu salario de R${:.2f}, foi ajustaco com 15% passando a R${:.2f}.'.format(salario,salario_ajustado))