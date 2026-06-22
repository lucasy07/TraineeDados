lista = ["arroz", "feijão", "macarrão"]

lista.append("açúcar")  
lista.insert(1, "óleo")  
outros_itens = ["sal", "pimenta"]
lista.extend(outros_itens)  
lista.remove("macarrão")  
x = lista.pop(-1)  
tamanho = len(lista)  

print(lista)  
print(x)  
print(tamanho) 
