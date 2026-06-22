clientes = {
    'cliente1': {
    'nome': 'Ana Paula',
    'idade': 32,
    'email': 'ana@email.com',
    'cidade': 'São Paulo'
    },
    'cliente2': {
    'nome': 'Roberto Lima',
    'idade': 45,
    'email': 'roberto@email.com',
    'cidade': 'Rio de Janeiro'
    },
    'cliente3': {
    'nome': 'Mariana Rocha',
    'idade': 28,
    'email': 'mariana@email.com',
    'cidade': 'Curitiba'
    }       
}

print(f"Idade do cliente1: {clientes['cliente1']['idade']}")
print(f"Email do cliente2: {clientes['cliente2']['email']}")

clientes['cliente1']['idade'] = 33

clientes["cliente4"] = {"nome": "Diego Costa","idade": 35,"email": "diegocosta@gmail.com","cidade": "Belo Horizonte"}

for i in clientes:
    print(clientes[i])

del clientes['cliente2']
