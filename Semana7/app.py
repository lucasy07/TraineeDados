
import streamlit as st
import pandas as pd

# Configura a aba do navegador e usa a largura toda da tela.
st.set_page_config(page_title="Explorador de CSV", layout="wide")

st.title("Explorador de CSV")

@st.cache_data
def carregar(arquivo):
    return pd.read_csv(arquivo)


# file_uploader retorna o arquivo enviado, ou None enquanto ninguém subiu nada.
arquivo = st.file_uploader("Suba um CSV", type="csv")

if arquivo is None:
    st.info("Suba um arquivo CSV para começar.")
    st.stop()  # interrompe o rerun aqui; nada abaixo executa sem arquivo

df = carregar(arquivo)

# --- Métricas: dois números lado a lado ---
col1, col2 = st.columns(2)
col1.metric("Linhas", df.shape[0])
col2.metric("Colunas", df.shape[1])

# --- Tabela com os dados ---
st.subheader("Dados")
st.dataframe(df, use_container_width=True)

# --- Filtro por coluna numérica ---
st.subheader("Filtro")

# Pega só as colunas numéricas
colunas_num = df.select_dtypes(include="number").columns.tolist()

if colunas_num:
    coluna = st.selectbox("Coluna numérica para filtrar", colunas_num)

    minimo = float(df[coluna].min())
    maximo = float(df[coluna].max())
    faixa = st.slider("Faixa de valores", minimo, maximo, (minimo, maximo))

    df_filtrado = df[df[coluna].between(faixa[0], faixa[1])]

    st.write(f"{df_filtrado.shape[0]} linha(s) dentro do filtro")
    st.dataframe(df_filtrado, use_container_width=True)

    # --- Gráfico da coluna filtrada ---
    st.subheader("Gráfico")
    st.bar_chart(df_filtrado[coluna])
else:
    st.warning("Nenhuma coluna numérica encontrada para filtrar.")