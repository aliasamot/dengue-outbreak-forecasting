import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.markdown(
    """
    <style>
    .main {
        background-color: #FFF4EA;
    }
    </style>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap');
    
    /* Button styles */
    .stButton > button {
        background-color: #982B1C; 
        border-radius: 12px;
        padding: 10px 24px;
        color: white; /* Text color */
        font-size: 16px;
        font-family: 'Quicksand', sans-serif;
        font-weight: bold;
        border: none; 
    }

    /* Hover effect for buttons */
    .stButton > button:hover {
        background-color: #800000; 
        color: white; 
    }

    /* Header style */
    header {
        background-color: #800000;
        padding: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    header h1 {
        font-family: 'Libre Baskerville', sans-serif;
        font-size: 2em;
        color: white;
        text-shadow: 1px 1px 2px #000000;
        margin: 0;
    }
    
    h3 {
        font-family: 'Libre Baskerville', sans-serif;
        font-size: 2em;
        color: #800000;
        justify-content: center;
    }

    p {
        font-family: "Quicksand", system-ui;
        font-size: 1em;
        line-height: 1.5em;
        color: black;
    }

    /* Footer styles */
    footer {
        font-family: "Quicksand", system-ui;
        text-align: center;
        padding: 15px;
        background-color: #800000;
        color: white;
        margin-top: 20px;
        font-size: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit interface
st.markdown(f"""
<header>
    <h1>Linear Regression Analysis for Amount of Waste</h1>
</header>
""", unsafe_allow_html=True)

# Initialize session state
if 'model' not in st.session_state:
    st.session_state.model = None
if 'b0' not in st.session_state:
    st.session_state.b0 = None
if 'b1' not in st.session_state:
    st.session_state.b1 = None
if 'data' not in st.session_state:
    st.session_state.data = None

# Upload dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type="csv")

if uploaded_file is not None:
    # Read the file into a pandas DataFrame
    st.session_state.data = pd.read_csv(uploaded_file)
    st.write(st.session_state.data)  # Display the DataFrame

    # Automatically convert columns with commas or non-numeric characters into numeric
    for col in st.session_state.data.columns:
        st.session_state.data[col] = pd.to_numeric(st.session_state.data[col].astype(str).str.replace(',', ''), errors='coerce')

    # Select dependent and independent variables
    numeric_columns = st.session_state.data.select_dtypes(include=[np.number]).columns
    x_var = st.selectbox("Select the independent variable (X)", numeric_columns)  
    dep_var = st.selectbox("Select the dependent variable (y)", numeric_columns)

    # Perform regression when button is clicked
    if st.button("Calculate Regression Coefficients"):
        # Reshape the data for the model
        X = st.session_state.data[[x_var]].values
        y = st.session_state.data[dep_var].values

        # Create a linear regression model
        st.session_state.model = LinearRegression()
        st.session_state.model.fit(X, y)

        # Get coefficients
        st.session_state.b0 = st.session_state.model.intercept_  # Intercept
        st.session_state.b1 = st.session_state.model.coef_[0]    # Slope

        # Display coefficients and equation
        st.write(f"Intercept (b0): {st.session_state.b0}")
        st.write(f"Coefficient for {x_var} (b1): {st.session_state.b1}")

        # Display the regression equation
        equation = f"{dep_var} = {st.session_state.b0} + {st.session_state.b1} * {x_var}"
        st.write(f"Calculated Regression Equation: {equation}")

        # Calculate predicted values
        st.session_state.data['Predicted_' + dep_var] = st.session_state.model.predict(X)

        # Calculate MSE and R²
        mse = mean_squared_error(y, st.session_state.data['Predicted_' + dep_var])
        r2 = r2_score(y, st.session_state.data['Predicted_' + dep_var])

        # Display MSE and R²
        st.write(f"Mean Squared Error (MSE): {mse:}")
        st.write(f"R-squared (R²): {r2:}")

        # Create a scatter plot with the regression line
        plt.figure(figsize=(10, 6))
        plt.scatter(X, y, color='blue', label='Data Points')
        plt.plot(X, st.session_state.data['Predicted_' + dep_var], color='red', linewidth=2, label='Regression Line')
        plt.title('Scatter Plot with Regression Line')
        plt.xlabel(x_var)
        plt.ylabel(dep_var)
        plt.legend()
        st.pyplot(plt)  # Display the plot in Streamlit
        plt.clf()  # Clear the plot to avoid overlap in future plots

# Prediction form
if st.session_state.b0 is not None and st.session_state.b1 is not None:
    st.markdown("### Predict using new value:")
    
    with st.form(key='prediction_form'):
        new_x = st.number_input(f"Enter new value for X", format="%.5f", value=0.0)
        
        # Submit button
        submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            # Calculate the predicted value
            predicted_y = st.session_state.b0 + st.session_state.b1 * new_x
            
            # Display the prediction result
            st.write(f"Predicted value for {dep_var}: {predicted_y:}")

if st.button("Home"):
    st.switch_page("Home.py")
