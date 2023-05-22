import streamlit as st
import pickle
import numpy as np

# Load the model into memory
with open('/content/drive/MyDrive/model_pognali/new_model.pkl', 'rb') as model_pkl:
    lr = pickle.load(model_pkl)

# Create a text input for the user to enter the value for the unseen variable
unseen = st.text_input('Enter the value for the unseen variable:', 45.367)

# Convert the input to a float and create a test observation
X_test_sm = [[float(1.0)], [float(unseen)]]
X_test_sm = np.squeeze(X_test_sm)

# Make a prediction using the model
result = lr.predict(X_test_sm)[0]

# Display the result
st.write(f'При количестве безработных {float(unseen)*1000:.0f}, количество алкоголиков будет составлять {result*1000:.0f}')
