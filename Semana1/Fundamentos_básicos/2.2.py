emails = input("Digite tres emails: ").split()

for i in emails:
    if i == "":
        print("Email inválido!")
    elif "@" not in i or not (i.endswith(".com") or i.endswith(".com.br")):
        print ("Email inválido!")
    else:
        print("Email válido!")
