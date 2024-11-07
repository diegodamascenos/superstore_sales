from pathlib import Path
import pandas as pd

import streamlit as st

pasta_superstore_sales = Path(__file__).parent.parent / 'superstore_sales'
caminho_superstore = pasta_superstore_sales / 'train.csv'

df_train = pd.read_csv('train.csv', decimal=',')

colunas = list(df_train.columns)
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas', colunas, colunas)

col1, col2 = st.sidebar.columns(2)
col_filtro = col1.selectbox('Selecione a coluna', [c for c in colunas if c not in ['Row ID']])
valor_filtro = col2.selectbox('Selecione o valor', list(df_train[col_filtro].unique()))

status_filtrar = col1.button('Filtrar')
status_limpar = col2.button('Limpar')

if status_filtrar:
    st.dataframe(df_train.loc[df_train [col_filtro] == valor_filtro, colunas_selecionadas], height=800)
elif status_limpar:
    st.dataframe(df_train[colunas_selecionadas], height=800)
else:
    st.dataframe(df_train[colunas_selecionadas], height=800)