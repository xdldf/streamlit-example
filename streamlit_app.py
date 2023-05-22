import streamlit as st
import pickle
import numpy as np
import pandas as pd
# Load the model into memory
with open('new_model.pkl', 'rb') as model_pkl:
    lr = pd.read_pickle(model_pkl)

# Create a text input for the user to enter the value for the unseen variable
unseen = st.text_input('Введите количество безработных (тыс. человек):', 0)

# Convert the input to a float and create a test observation
X_test_sm = [[float(1.0)], [float(unseen)]]
X_test_sm = np.squeeze(X_test_sm)

# Make a prediction using the model
result = lr.predict(X_test_sm)[0]

# Display the result
if result < 0:
    st.write(f'При количестве безработных в {float(unseen)} тыс. человек, алкоголиков не будет')
else:
    st.write(f'При количестве безработных в {float(unseen)} тыс. человек, количество алкоголиков будет составлять {result} тыс. человек')

import streamlit as st
import pandas as pd
import plotly.express as px

# Создание DataFrame с данными для точечного графика
df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 30, 40]
})

# Создание точечного графика с помощью Plotly Express
fig = px.scatter(df, x='x', y='y')

# Добавление возможности изменения значений точек с помощью мышки
fig.update_traces(mode='markers', marker={'size': 15}, 
                  dragmode='select', selected={'marker': {'opacity': 1}}, 
                  unselected={'marker': {'opacity': 0.3}})

# Отображение графика в Streamlit
st.plotly_chart(fig)
