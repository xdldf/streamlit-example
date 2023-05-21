import streamlit as st
import plotly.graph_objs as go

# Создание данных для графика
x_values = list(range(10))
y_values = list(range(10))

# Создание графика с помощью Plotly
fig = go.FigureWidget([go.Scatter(x=x_values, y=y_values, mode='markers')])

# Функция для обновления данных на графике при перетаскивании точек мышью
def update_point(trace, points, selector):
    for i in points.point_inds:
        x_values[i] = points.xs[i]
        y_values[i] = points.ys[i]

# Добавление обработчика событий для обновления данных на графике при перетаскивании точек мышью
fig.data[0].on_click(update_point)

# Отображение графика в Streamlit
st.plotly_chart(fig)
