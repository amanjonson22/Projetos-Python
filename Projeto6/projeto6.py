def MinMax (temperaturas):
    print("A menor temperatura do mês foi:", mínima(temperaturas), 'C.')
    print('A maior temperatura do mês foi:', máxima(temperaturas), 'C.')

def mínima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i]< min:
            min = temps[i]
        i = i+1
    return min

def máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i+1
    return max

def teste_pontual(temp, valor_esperado):
    valor_calculado = mínima(temp)
    if valor_calculado != valor_esperado:
        print('Valor errado para array', temp)
        print('Valor esperado: ', valor_esperado, '. Valor calculado: ', valor_calculado)

def teste_pontual_max(temp, valor_esperado):
    valor_calculado = máxima(temp)
    if valor_calculado != valor_esperado:
        print('Valor errado para array', temp)
        print('Valor esperado: ', valor_esperado, '. Valor calculado: ', valor_calculado)

def testa_mínima():
    print('Iniciando testes - Mínima')
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
    teste_pontual([30, 27,25, 26, 29, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 24, 22, 23, 25, 25, 28, 28, 32, 31, 29, 28, 31, 33], 22)
    teste_pontual ([-15, -12, 2, 10, 1, 0, -18, 7, 3, -20], -20)
    print('Finalizando testes - Mínima')

def testa_máxima():
    print('Iniciando testes - Máxima')
    teste_pontual_max([25], 25)
    teste_pontual_max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    teste_pontual_max([30, 27,25, 26, 29, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 24, 22, 23, 25, 25, 28, 28, 32, 31, 29, 28, 31, 33], 33)
    teste_pontual_max ([-15, -12, 2, 10, 1, 0, -18, 7, 3, -20], 10)
    print('Finalizando testes - Máxima')

testa_mínima()
testa_máxima()

MinMax([2, 7, 7, 4, -2, 0, -5, -7, -2, 2, 4, 5, 8, 9, 10, 2, -8, -9, -8, -5, -3, 0, 1, 2, 4, 2, 1, 0, -3, 4, 5, 10, 11, 2, 0])