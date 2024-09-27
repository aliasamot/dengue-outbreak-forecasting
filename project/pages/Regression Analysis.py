import streamlit as st
import pandas as pd
import numpy as np

st.markdown(
    """
    <style>
    .main {
        background-color: #FFF4EA
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
        font-size: 2.3em;
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

def calculate_regression_coefficients(data, x1, x2, x3, dep_var):
    try:
        # Extracting X (independent variables) and y (dependent variable)
        x1 = data[x1].values
        x2 = data[x2].values
        x3 = data[x3].values
        y = data[dep_var].values
        n = len(data)

        # Calculate the sums required by the formula
        sum_y = y.sum()
        sum_x1 = x1.sum()
        sum_x2 = x2.sum()
        sum_x3 = x3.sum()

        sum_x1_x1 = (x1 ** 2).sum() - (sum_x1 * sum_x1) / n
        sum_x2_x2 = (x2 ** 2).sum() - (sum_x2 * sum_x2) / n
        sum_x3_x3 = (x3 ** 2).sum() - (sum_x3 * sum_x3) / n

        sum_x1_x2 = (x1 * x2).sum() - (sum_x1 * sum_x2) / n
        sum_x1_x3 = (x1 * x3).sum() - (sum_x1 * sum_x3) / n
        sum_x2_x3 = (x2 * x3).sum() - (sum_x2 * sum_x3) / n

        sum_x1_y = (x1 * y).sum() - (sum_x1 * sum_y) / n
        sum_x2_y = (x2 * y).sum() - (sum_x2 * sum_y) / n
        sum_x3_y = (x3 * y).sum() - (sum_x3 * sum_y) / n

        # Create matrices for the multiple regression model (without intercept row)
        X_matrix = np.array([
            [sum_x1_x1, sum_x1_x2, sum_x1_x3],
            [sum_x1_x2, sum_x2_x2, sum_x2_x3],
            [sum_x1_x3, sum_x2_x3, sum_x3_x3]
        ])

        Y_matrix = np.array([
            [sum_x1_y],
            [sum_x2_y],
            [sum_x3_y]
        ])

        # Solve for the coefficients (B1, B2, B3) using matrix inversion
        B = np.linalg.inv(X_matrix) @ Y_matrix

        # Calculate the intercept (b0)
        b0 = sum_y/n - (B[0] * sum_x1/n) - (B[1] * sum_x2/n) - (B[2] * sum_x3/n)

        # Return the coefficients B0 (intercept), B1, B2, B3
        return b0, B[0], B[1], B[2], n

    except KeyError as e:
        st.error(f"Column '{e.args[0]}' not found in the dataset.")
        return None, None, None, None, None

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None, None, None, None
    
# Streamlit interface
st.markdown(f"""
<header>
    <h1>Regression Analysis</h1>
</header>
""", unsafe_allow_html=True)

# Upload dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the file into a pandas DataFrame
    data = pd.read_csv(uploaded_file)
    st.write(data)  # Display the DataFrame

    # Automatically convert columns with commas or non-numeric characters into numeric
    for col in data.columns:
        data[col] = pd.to_numeric(data[col].astype(str).str.replace(',', ''), errors='coerce')

    # Select dependent and independent variables
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    x1 = st.selectbox("Select the first independent variable (X1)", numeric_columns)  
    x2 = st.selectbox("Select the second independent variable (X2)", numeric_columns)  
    x3 = st.selectbox("Select the third independent variable (X3)", numeric_columns)  
    dep_var = st.selectbox("Select the dependent variable (y)", numeric_columns)

    # Perform regression when button is clicked
    if st.button("Calculate Regression Coefficients"):
        b0, b1, b2, b3, n = calculate_regression_coefficients(data, x1, x2, x3, dep_var)
        
        if b0 is not None and b1 is not None and b2 is not None and b3 is not None:
            # Store coefficients in session state to access during prediction
            st.session_state.b0 = b0[0]
            st.session_state.b1 = b1[0]
            st.session_state.b2 = b2[0]
            st.session_state.b3 = b3[0]

            # Display coefficients and equation
            st.write(f"Intercept (b0): {st.session_state.b0}")
            st.write(f"Coefficient for {x1} (b1): {st.session_state.b1}")
            st.write(f"Coefficient for {x2} (b2): {st.session_state.b2}")
            st.write(f"Coefficient for {x3} (b3): {st.session_state.b3}")

            # Display the regression equation
            equation = f"{dep_var} = {st.session_state.b0} + {st.session_state.b1}*{x1} + {st.session_state.b2}*{x2} + {st.session_state.b3}*{x3}"
            st.write(f"Calculated Regression Equation: {equation}")

            # Calculate MSE and R² for the entire dataset using the predicted values
            data['Predicted_' + dep_var] = (st.session_state.b0 + 
                                             st.session_state.b1 * data[x1] + 
                                             st.session_state.b2 * data[x2] + 
                                             st.session_state.b3 * data[x3])

            # Calculate residuals
            residuals = data[dep_var] - data['Predicted_' + dep_var]

            # Mean Squared Error
            mse = (1 / n) * (residuals ** 2).sum()

            # R-squared
            r2 = 1 - (residuals ** 2).sum() / ((data[dep_var] - data[dep_var].mean()) ** 2).sum()

            # Display MSE and R²
            st.write(f"Mean Squared Error (MSE): {mse:}")
            st.write(f"R² (Coefficient of Determination): {r2:}")
            
# Ensure that the prediction form is only shown if the coefficients have been computed
if 'b0' in st.session_state and 'b1' in st.session_state and 'b2' in st.session_state and 'b3' in st.session_state:
    # Prediction form
    st.markdown("### Predict using new values:")
    
    with st.form(key='prediction_form'):
        new_x1 = st.number_input(f"Enter new value for X1", format="%.5f", value=0.0)
        new_x2 = st.number_input(f"Enter new value for X2", format="%.5f", value=0.0)
        new_x3 = st.number_input(f"Enter new value for X3", format="%.5f", value=0.0)
        
        # Submit button
        submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            # Calculate the predicted value using the stored coefficients
            predicted_y = (st.session_state.b0 + 
                           st.session_state.b1 * new_x1 + 
                           st.session_state.b2 * new_x2 + 
                           st.session_state.b3 * new_x3)
            
            # Display the prediction result
            st.write(f"Predicted value for {dep_var}: {predicted_y:}")

if st.button("Home"):
    st.switch_page("Home.py")
