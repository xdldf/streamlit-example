import streamlit as st
import plotly.express as px
import pandas as pd

# Создаем DataFrame с данными о безработице
data = {'Year': [2022, 2023],
        'Unemployment': [5.0, 4.5]}
df = pd.DataFrame(data)

# Добавляем виджет для выбора значения безработицы
unemployment = st.slider('Select Unemployment Rate', min_value=0.0, max_value=10.0, value=5.0)

# Обновляем данные в DataFrame
df.loc[df['Year'] == 2022, 'Unemployment'] = unemployment

# Создаем интерактивный график с плавающими точками
fig = px.scatter(df, x='Year', y='Unemployment', title='Unemployment Rate')
fig.update_traces(mode='markers+lines')
st.plotly_chart(fig)
