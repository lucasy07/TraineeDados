nome = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF: ")
nascimento = input("Digite sua data de nascimento: ")
salario = float(input("Digite seu salário em R$: "))
ativo = input("É funcionário ativo?(Sim/Não): ").strip().lower() == "sim"

print("=== RELATÓRIO DE CADASTRO ===")
print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"CPF: {cpf} (tipo: {type(cpf)})")
print(f"Data de nascimento: {nascimento} (tipo: {type(nascimento)})")
print(f"Salário: R$ {salario} {type(salario)}")

if(ativo == "sim"):
    print(f"Status: Ativo (tipo: {type(ativo)})")
else:
    print(f"Status: Inativo (tipo: {type(ativo)})")

print("=============================")
