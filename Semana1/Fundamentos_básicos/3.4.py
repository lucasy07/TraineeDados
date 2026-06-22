preco = float(input("Valor: "))
vip = input("VIP: ").strip().lower() == "sim"

desconto = 0.0

if vip:
    desconto = 0.02

if 100 < preco <= 500:
    desconto += 0.05
elif 500 < preco <= 1000:
    desconto += 0.10
elif preco > 1000:
    desconto += 0.15

valor_desconto = preco * desconto
resultado = preco - valor_desconto

print(f"Valor original: R$ {preco:.2f}")
print(f"Desconto aplicado: {desconto:.2%}")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Valor final: R$ {resultado:.2f}")
