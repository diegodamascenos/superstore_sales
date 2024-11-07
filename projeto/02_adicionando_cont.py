from pathlib import Path

import streamlit as st
import pandas as pd

pasta_superstore_sales = Path(__file__).parent.parent / 'superstore_sales'
caminho_superstore = pasta_superstore_sales / 'train.csv'

df_train = pd.read_csv('train.csv', decimal=',')
df_train['City/State'] = df_train['City']
lista_filiais = df_train['City/State'].tolist()
st.sidebar.selectbox('Selecione a região:', lista_filiais)

st.dataframe(df_train)