idade = int(input("Digite sua idade: "))
possui_carteira = input("Possui carteira? ").strip().lower() == "sim"
esta_suspensa = input("Está suspensa? ").strip().lower() == "sim"

if idade >= 18 and possui_carteira and not esta_suspensa:
    print("Pode dirigir!")
else:
    print("Não pode dirigir!")
