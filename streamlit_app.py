import streamlit as st
import plotly.graph_objects as go

fig = go.Figure()

for i in range(10):
    fig.add_trace(go.Scatter(x=[i], y=[i], mode='markers', marker=dict(size=10)))

fig.update_layout(
    xaxis=dict(range=[-1, 11]),
    yaxis=dict(range=[-1, 11]),
    dragmode='pan',
    hovermode='closest'
)

st.plotly_chart(fig)
