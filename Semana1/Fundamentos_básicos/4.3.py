i = False

while i == False:
    senha = input("Digite uma senha: ")
    maiuscula = False
    minuscula = False
    numero = False

    if len(senha) >= 8:
        for j in senha:
            if(j.isupper()):
                maiuscula = True
            if(j.islower()):
                minuscula = True
            if(j.isnumeric()):
                numero = True
        if maiuscula and minuscula and numero:
            i == True
            print("Senha válida: Cadastro realizado com sucesso")
            break
        else:
            print("Senha inválida! Tente novamente")
    else:
        print("Senha inválida! Tente novamente")
    
