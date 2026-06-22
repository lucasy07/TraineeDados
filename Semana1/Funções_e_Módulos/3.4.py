def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b
    
def calcular(num1, num2, operacao):
    if operacao == '+':
        return somar(num1, num2)
    elif operacao == '-':
        return subtrair(num1, num2)
    elif operacao == '*':
        return multiplicar(num1, num2)
    elif operacao == '/':
        return dividir(num1, num2)
    
print(calcular(10, 5, "+"))
print(calcular(10, 5, "-"))
print(calcular(10, 5, "*"))
print(calcular(10, 5, "/"))
print(calcular(10, 0, "/"))
