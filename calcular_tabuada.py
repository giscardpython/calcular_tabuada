def calcular_tabuada(x, y):
    soma = x + y
    yield soma
    subtração = x - y
    yield subtração
    multiplicação = x * y
    yield multiplicação
    divisão = x / y
    yield divisão

# programa principal
#tupla = ('soma', 'substração', 'multiplicação', 'divisão')

x = int(input('Informe o primeiro valor: '))
y = int(input('Informe o segundo valor: '))
resultados = calcular_tabuada (x, y)

#for resultado in resultados:
#    print (resultado)

print(f'A soma é {next(resultados)}.')    
print(f'A subtração é {next(resultados)}.')    
print(f'A multiplicação é {next(resultados)}.')    
print(f'A divisão é {next(resultados)}.')    