somar = lambda a, b: a + b
subtrair = lambda a, b: a - b
multiplicar = lambda a, b: a * b
dividir = lambda a, b: 0 if b == 0 else a / b

operacoes = [somar, subtrair, multiplicar, dividir]

def aplicar_operacoes(x, y):
    resultados = []
    for op in operacoes:
        resultados.append(op(x, y))
    return resultados

print(aplicar_operacoes(20, 4))
