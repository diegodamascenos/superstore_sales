from pathlib import Path

import streamlit as st
import pandas as pd

pasta_superstore_sales = Path(__file__).parent / 'superstore_sales'
df_train = pd.read_csv(pasta_superstore_sales / 'train.csv', decimal=',')
df_products = pd.read_csv(pasta_superstore_sales / 'products.csv', decimal=',')
df_customers = pd.read_csv(pasta_superstore_sales / 'customers.csv', decimal=',')

st.dataframe(df_train)
st.dataframe (df_products)
st.dataframe(df_customers)