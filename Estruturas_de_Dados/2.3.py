frutas1 = ('maçã', 'banana', 'laranja')
frutas2 = ('uva', 'morango', 'abacaxi', 'kiwi')

todas_frutas = frutas1 + frutas2
print(todas_frutas)

for fruta in todas_frutas:
    print(fruta, end=" ")

print()

numeros = (1, 2, 3, 2, 4, 2, 5)

x = numeros.count(2)
print(f"Quantas vezes 2 aparece: {x}")

n = todas_frutas.index("abacaxi")
print(f"Índice do primeiro abacaxi: {n}")

tamanho = len(todas_frutas)
print(f"Tamanho da tupla: {tamanho}")
