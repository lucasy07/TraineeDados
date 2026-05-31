cores = ("vermelho", "azul", "verde", "amarelo")

# cores[1] = "laranja" - erro

lista = list(cores)

lista[1] = "roxo"
print(lista)

(cor1, cor2, cor3, cor4) = cores
print(f"Desempacotamento: cor1 = {cor1}, cor2 = {cor2}, cor3 = {cor3}, cor4 = {cor4}")

new_cores = ("laranja", "rosa", "preto", "branco", "cinza")

(c1, c2, *resto) = new_cores
print(f"Desempacotamento com *: c1 = {c1}, c2 = {c2}, resto = {resto}")
