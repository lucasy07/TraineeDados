import streamlit as st
import pandas as pd
import numpy as np
import joblib

art = joblib.load("modelo.joblib")
lasso, xgb, W = art["lasso"], art["xgb"], art["w"]
cols, base, skewed = art["cols"], art["median_row"], set(art["skewed"])

def preencher(row, col, valor):
    """Aplica a MESMA transformação do treino antes de gravar."""
    if col in skewed:
        valor = np.log1p(valor)      # feature enviesada foi logada no treino
    row[col] = valor

st.title("Simulador de preço de imóveis — Ames, Iowa")
st.caption("As demais características são fixadas na mediana do conjunto de treino.")

bairros = sorted(c.replace("Neighborhood_", "") for c in cols
                 if c.startswith("Neighborhood_"))

col1, col2 = st.columns(2)
with col1:
    total_sf = st.slider("Área total (pés²)", 500, 6000, 2500, step=50)
    qual     = st.slider("Qualidade geral (1-10)", 1, 10, 6)
    banhos   = st.slider("Banheiros (equivalente)", 1.0, 5.0, 2.0, step=0.5)
with col2:
    idade    = st.slider("Idade na venda (anos)", 0, 130, 30)
    garagem  = st.slider("Vagas de garagem", 0, 4, 2)
    bairro   = st.selectbox("Bairro", bairros)

# monta a linha de 265 colunas a partir da casa mediana
row = base.copy()
preencher(row, "TotalSF", total_sf)
preencher(row, "OverallQual", qual)
preencher(row, "TotalBath", banhos)
preencher(row, "HouseAge", idade)
preencher(row, "GarageCars", garagem)

for c in cols:                                  # zera todos os bairros...
    if c.startswith("Neighborhood_"):
        row[c] = 0
row[f"Neighborhood_{bairro}"] = 1               # ...e liga só o escolhido

entrada = pd.DataFrame([row])[cols]             # ordem idêntica à do treino

pred_log = W * lasso.predict(entrada) + (1 - W) * xgb.predict(entrada)
preco = float(np.expm1(pred_log)[0])            # desfaz o log -> dólares

st.metric("Preço estimado", f"$ {preco:,.0f}")
st.caption("Estimativa de modelo (RMSE ≈ 0.123 em log, validação cruzada). "
           "Não é avaliação imobiliária.")