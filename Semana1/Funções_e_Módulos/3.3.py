def criar_produto(nome, preco, quantidade):
    total = preco * quantidade
    dict = {
        "nome" : nome,
        "preco" : preco,
        "quantidade" : quantidade,
        "total" : total
    }

    return dict

produto1 = criar_produto("Notebook", 2500.00, 5)
print(produto1)

produto2 = criar_produto("Mouse", 50.00, 20)
print(produto2)
