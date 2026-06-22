pessoa = {
    "nome": "Sakurajima Mai",
    "idade": 18,
    "altura": 1.65,
    "habilitado": True,
}

print(f"Dicionário: {pessoa}")
print(f"Tipo: {type(pessoa)}")
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Altura: {pessoa['altura']}")
print(f"Habilitado: {pessoa['habilitado']}")
      
pessoa["idade"] = 29
pessoa["cidade"] = "Tokyo"

print()

print(f"Dicionário modificado: {pessoa}")
print(f"Tipo: {type(pessoa)}")
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Altura: {pessoa['altura']}")
print(f"Habilitado: {pessoa['habilitado']}")
print(f"Cidade: {pessoa['cidade']}")

print(f"Tamanho: {len(pessoa)}")
