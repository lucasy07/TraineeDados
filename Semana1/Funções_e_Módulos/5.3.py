frase = "Python é uma linguagem de programação"

maiusculas = [palavra.upper() for palavra in frase.split()]
comprimentos = [len(palavra) for palavra in frase.split()]

print(maiusculas)
print(comprimentos)
