def criar_perfil(**kwargs):
    print("=== Perfil ===")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
    print("---")

criar_perfil(nome="João", idade=25, cidade="São Paulo", profissao="Desenvolvedor")
criar_perfil(nome="Maria", idade=30, email="maria@email.com")
