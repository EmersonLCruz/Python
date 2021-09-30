# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(valor,show=False):
    """ -> Calcula valor Fatorial de n
        Param valor: recebe valor para calculo de fatorial
        Param show: (OPCIONAL) mostra como o calculo foi realizado
        return: retorna o resultado do fatorial de n
    """
    fat = 1
    if show == True:
        #print(fat,end=' x ')
        for x in range(valor,0,-1):
            if x == 1:
                print(x,end=' = ')
                break
            print(x,end=' x ')
            fat *= x
    else:
        for x in range(valor,0,-1):
            fat *= x
    return fat
            


print(fatorial(5))
print(fatorial(5,True))