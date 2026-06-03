def exibir_menu():
    while True:
        print("A. Mensagem de boas vindas")
        print("B. Mensagem de despedida")
        print("C. Mensagem personalizada")
        print("D. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == 'A':
            mensagem_boas_vindas()
        elif escolha == 'B':
            mensagem_despedida()
        elif escolha == 'C':
            mensagem_personalizada()
        else:
            break

def mensagem_boas_vindas():
    print("Bem-vindo ao sistema!")
    print()

def mensagem_despedida():
    print("Obrigado por usar o sistema!")
    print()

def mensagem_personalizada():
    nome = input("Como devo lhe chamar? ")
    print(f"Olá {nome}! Como posso ajudar?")
    print()

exibir_menu()
