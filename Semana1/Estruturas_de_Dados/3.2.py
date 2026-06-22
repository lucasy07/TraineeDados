produto = {
    'nome': 'Notebook',
    'preco': 2500.00,
    'estoque': 10
}


print(f"Preço(get): {produto.get("preco")}")

print(f"Desconto(get): {produto.get("desconto")}")

if "estoque" in produto:
    print("Estoque existe")
else:
    print("Estoque não existe")

produto.update({"preco": 2200.00, "categoria": "eletronicos"})

estoque = produto.pop("estoque")
print(f"Valor do estoque: {estoque}")

produto.popitem()
print(f"Após remoção {produto}")
