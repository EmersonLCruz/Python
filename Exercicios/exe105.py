# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
def notas(*n,situacao=False):
    '''
    -> Função para analisar notas e situação de varios alunos:
    param: n: Recebe várias notas
    param: situacao: Indica se o retorno da função deve vir explicitando o campo "Situação"
    return: returna as seguintes informações
     Quantidade de notas
     A maior nota
     A menor nota
     A média da turma
     A situação (opcional) 
    '''
    relatorio_notas = {}
    soma = 0
    relatorio_notas['Total'] = len(n)
    relatorio_notas['Maior'] = max(n)
    relatorio_notas['Menor'] = min(n)
    for nota in n:
        soma += nota
    relatorio_notas['Media'] = soma / len(n)
    if relatorio_notas['Media'] < 3:
        relatorio_notas['Situacao'] = 'Regular'
    elif 3 <= relatorio_notas['Media'] < 7:
        relatorio_notas['Situacao'] = 'Bom'
    else:
        relatorio_notas['Situacao'] = 'Otimo'
    if situacao:
        return relatorio_notas
    else:
        del relatorio_notas['Situacao']
        return relatorio_notas



help(notas)
resp = notas(1.5,3,2.8,0,2)
print(resp)