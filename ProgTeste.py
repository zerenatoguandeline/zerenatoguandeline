import streamlit as st
import pandas as pd
import numpy as np

# Título da aplicação
st.title("📊 Dashboard de Análise Econômica")

# Criando um seletor na barra lateral
indicador = st.sidebar.selectbox(
    "Selecione o indicador para visualizar:",
    ("PIB", "IPCA", "Selic")
)

st.write(f"Exibindo dados simulados para: **{indicador}**")

# Gerando dados aleatórios para o gráfico
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Agro', 'Varejo', 'Transporte']
)

# Criando o gráfico interativo
st.line_chart(data)

# Adicionando uma tabela de dados
if st.checkbox('Mostrar dados brutos'):
    st.subheader('Dados brutos')
    st.write(data)
