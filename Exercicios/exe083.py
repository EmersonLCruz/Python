# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = [input('Digite sua expressão: ')]
print(expressao)
parentese_aberto = expressao[0].count('(')
parentese_fechado = expressao[0].count(')')
parentese_para_fechar = 0
if parentese_aberto == parentese_fechado:
    for x in expressao[0]:
        if x == ')' and parentese_para_fechar == 0:
            print('Expressão invalida')
            break
        elif x == '(':
            parentese_para_fechar += 1
            
        elif x == ')':
            parentese_para_fechar -= 1
            
    if parentese_para_fechar > 0:
        print('Expressão inválida')
    else:
        print('Expressão válida')
else:
    print('Expressão inválida')
    
'''pilha =[]
for item in expressao:
    if item == '(':
        pilha.append('(')
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print(pilha)
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('expressão inválida')  '''