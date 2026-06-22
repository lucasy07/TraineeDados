def gerar_numeros_pares(n):
    pares = []
    for i in range(1, n + 1):
        pares.append(i * 2)
    return pares

print(gerar_numeros_pares(5))
print(gerar_numeros_pares(10))
