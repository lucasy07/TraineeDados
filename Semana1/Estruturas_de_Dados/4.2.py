conjunto1 = {'a', 'b', 'c'}
conjunto2 = {'c', 'd', 'e'}

conjunto1.update(conjunto2)

conjunto3 = {'f', 'g'}

conjunto1.update(conjunto3)
print(conjunto1)

conjunto1.remove('a')

conjunto1.discard('z')
print(conjunto1)

copia = conjunto1.copy()

conjunto1.clear()

print(f"Original após clear: {conjunto1}")
print(f"Copia: {copia}")
