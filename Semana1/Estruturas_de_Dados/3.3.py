aluno = {
'nome': 'João',
'idade': 22,
'curso': 'Engenharia',
'nota': 8.5
}

print("Chaves:", end = " ")
for chave in aluno.keys():
    print(chave, end = ", ")


print("Valores:", end = " ")
for valor in aluno.values():
    print(valor, end = ", ")


for chave, valor in aluno.items():
    print(f"{chave}: {valor}")


print(aluno.keys())

copy = aluno.copy()

copy['nota'] = 9.0

print(f"Original: {aluno}")
print(f"Cópia: {copy}")


    
