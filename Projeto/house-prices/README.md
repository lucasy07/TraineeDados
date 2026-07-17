# House Prices - Advanced Regression Techniques

Pipeline completo de análise e predição de preços de imóveis em Ames, Iowa.
Projeto do trainee de Dados — CatiJr (UFSCar).

## Pipeline

1. **EDA** — distribuição do alvo, tratamento de dados faltantes
2. **Tratamento** — distinção entre missing informativo (`NaN` = "não tem" → `None`/`0`) e missing real (→ imputação por mediana do bairro)
3. **Feature engineering** — encoding ordinal (qualidades `Po<Fa<TA<Gd<Ex`), correção de assimetria (`log1p`), features derivadas (`TotalSF`, `HouseAge`, `TotalBath`)
4. **Modelagem** — baseline linear regularizado → ensembles → tuning
5. **Blend** — Lasso + XGBoost

## Resultados (RMSE em log, validação cruzada 5-fold)

| Modelo | RMSE | Desvio |
|---|---|---|
| RandomForest | 0.1418 | ±0.0186 |
| XGBoost (default) | 0.1374 | ±0.0179 |
| GradientBoosting | 0.1327 | ±0.0179 |
| Ridge | 0.1300 | ±0.0205 |
| Lasso | 0.1297 | ±0.0209 |
| XGBoost (tunado) | **0.1231** | — |
| Blend (25% Lasso + 75% XGB) | **0.1234** | — |

Métrica alinhada à competição: RMSE entre logaritmos, medido em CV local.

## Simulador (Streamlit)

App interativo que estima preço a partir de área, qualidade, banheiros, idade, garagem e bairro.
Demais features fixadas na mediana do treino.

## Como rodar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Baixe os dados na [página da competição](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) e coloque em `data/`.

Execute o `notebook.ipynb` (gera o `modelo.joblib`), depois:

```bash
streamlit run app.py
```

## Limitações

- Modelo subestima imóveis de alto padrão (regressão à média)
- Outliers conhecidos (`GrLivArea > 4000`) não foram tratados
- Diferenças entre modelos frequentemente dentro do desvio da CV — comparações lidas com cautela
- Busca de hiperparâmetros atingiu bordas do espaço explorado
- Simulador assume "casa mediana" nas features não controladas