tabuada = int(input('Digite valor inteiro:'))
print(('='*10+' TABUADA DE {} '+'='*10).format(tabuada))
for x in range (1,11):
    print('{} x {:2} = {}'.format(tabuada,x,tabuada * x))
