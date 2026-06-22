def somar_numeros(*args):
    soma = 0
    for i in args:
        soma += i
    print(f"Soma: {soma}")

somar_numeros(1, 2, 3)
somar_numeros(10, 20, 30, 40, 50)
somar_numeros(5)
