nome = "Notebook Gamer"
quantidade = 125
preco = 3299.99
desconto = 0.15

total_bruto = quantidade * preco
total_final = total_bruto * (1 - desconto)

print("========== RELATÓRIO DE VENDAS ==========")
print(f"Produto:  {nome:^20}")
print(f"Quantidade:  {quantidade:03d} unidades")
print(f"Preço Unit.: R$ {preco:.2f}")
print(f"Desconto:    {desconto:.2%}")
print(f"Total Bruto: R$ {total_bruto:,.2f}")
print(f"Total Final: R$ {total_final:,.2f}")
print("=========================================")
