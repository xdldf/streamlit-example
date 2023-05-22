import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.express as px
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
result = float('{:.3f}'.format(result))

# Display the result
if result < 0:
    st.write(f'При количестве безработных в {float(unseen)} тыс. человек, алкоголиков не будет')
else:
    st.write(f'При количестве безработных в {float(unseen)} тыс. человек, количество алкоголиков будет составлять {result} тыс. человек')

