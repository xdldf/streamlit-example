import streamlit as st
import plotly.express as px
import pandas as pd

data = {'year': [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032],
        'unemployment_rate': [5.5, 5.3, 5.1, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7, 3.5]}
df = pd.DataFrame(data)

fig = px.line(df, x='year', y='unemployment_rate', title='Unemployment rate from 2022 to 2032')
fig.update_traces(mode='lines+markers')
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1 year",
                     step="year",
                     stepmode="backward"),
                dict(count=5,
                     label="5 years",
                     step="year",
                     stepmode="backward"),
                dict(count=10,
                     label="10 years",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

st.plotly_chart(fig)
