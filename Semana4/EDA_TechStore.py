import pandas as pd
import matplotlib.pyplot as plt

#CARREGAR OS DADOS A PARTIR DO ARQUIVO vendas.csv
df = pd.read_csv('vendas.csv')

#EXIBIR INFORMAÇÕES BÁSICAS
#Mostrar as 5 primeiras linhas do dataset
print("5 primeiras linhas do dataset")
print(f"{df.head()}\n")

#Exibir o número total de registros
print("Numero total de registros")
print(f"{df['cliente'].count()}\n")

#Calcular a receita total (coluna quantidade multiplicada pela coluna preco_unitario)
receita_total = df['quantidade'] * df['preco_unitario']
df['receita_total'] = receita_total
print("Receita total: ")
print(f"{df['receita_total'].head()}\n")

#FAZER CONSULTAS ESPECÍFICAS
#Filtrar e exibir as vendas da categoria "Eletrônicos"
vendas_eletronicos = df[df['categoria'] == 'Eletrônicos']
print(f"{vendas_eletronicos}\n")

#Identificar e exibir o produto mais vendido (em quantidade)
produto_mais_vendido = (
    df.groupby('produto')['quantidade']
    .sum()
    .sort_values(ascending=False)
    .head(1)
)
print("Produto mais vendido:")  
print(produto_mais_vendido)

#Descobrir e exibir a região com maior valor de compras.
regiao_mais_compras = (
    df.groupby('regiao')['receita_total']
    .sum()
    .sort_values(ascending=False)
    .head(1)
)
print("Região com maior valor de compras:")  
print(regiao_mais_compras)

#Gráfico de barras mostrando a receita por categoria.
receita_categoria = (
    df.groupby('categoria')['receita_total']
    .sum()
    .sort_values(ascending=False)
)
plt.figure(figsize=(8, 5))
receita_categoria.plot(kind="bar")
plt.title("Receita por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Gráfico de linha mostrando a evolução das vendas por mês.
df["data"] = pd.to_datetime(df["data"])
df['mes'] = df['data'].dt.month
evolucao_vendas = (
    df.groupby('mes')['receita_total']
    .sum()
)
df['evolucao_vendas'] = evolucao_vendas

plt.figure(figsize=(10, 5))
plt.plot(evolucao_vendas.index, evolucao_vendas.values, marker="o")
plt.title("Evolução das Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
