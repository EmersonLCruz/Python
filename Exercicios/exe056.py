# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
print('='*60)
print('FORMULÁRIO'.center(60))
print('='*60)
soma = 0
homem_velho = 0
mulher_jovem =0
for x in range (1,5):
    print('{}ª PESSOA'.center(60).format(x))
    print('-'* 60)
    nome = input('Nome completo:')
    idade = int(input('Idade:'))
    print('''Informe o sexo conforme opções
    [M] MASCULINO
    [F] FEMININO''')
    sexo = input('sua opção:').strip().upper()
    # descobrir a média de idade do grupo
    soma += idade
    media = soma / x
    if sexo == 'M' and homem_velho == 0:
        homem_velho = idade
        homem_velho_nome = nome
    elif sexo == 'M' and homem_velho < idade:
        homem_velho = idade
        homem_velho_nome = nome
    if sexo == 'F' and idade < 20:
        mulher_jovem += 1
print('='*60)
print('RELATÓRIO'.center(60))
print('='*60)
print('O homem mais velho tem idade de {} anos e se chama {}'.format(homem_velho,homem_velho_nome))
print('Média de idade do grupo é de {} anos'.format(int(media)))
print('Existe {} mulheres com idade inferior a 20 anos'.format(mulher_jovem))
print('-'*60)
