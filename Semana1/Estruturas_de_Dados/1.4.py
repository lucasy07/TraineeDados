alunos = [
    ['Nome', 'Idade', 'Nota'], #0
    ['Ana', 20, 8.5], #1
    ['Bruno', 19, 7.0], #2
    ['Carla', 21, 9.0], #3
    ['Diego', 20, 6.5] #4
]

print(f"Idade do Bruno: {alunos[2][1]}")
print(f"Nota da Carla: {alunos[-2][-1]}")
alunos[4][2] = 7.5
print(f"Nova nota do Diego: {alunos[4][2]}")


for i in alunos:
    print(i)

for nome, idade, nota in alunos:
    print(f"{nome} tem {idade} anos e nota {nota}")

alunos.append(["Elena", 22, 8.0])

print(f"Aluna nova: {alunos[5]}")







