# Ensure that the prediction form is only shown if the coefficients have been computed
if 'b0' in st.session_state and 'b1' in st.session_state and 'b2' in st.session_state and 'b3' in st.session_state:
    # Prediction form
    st.markdown("### Predict using new values:")
    
    with st.form(key='prediction_form'):
        new_x1 = st.number_input(f"Enter new value for X1", value=0.0, format="%.6f", step=0.0001)
        new_x2 = st.number_input(f"Enter new value for X2", value=0.0, format="%.6f", step=0.0001)
        new_x3 = st.number_input(f"Enter new value for X3", value=0.0, format="%.6f", step=0.0001)
        
        # Submit button
        submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            # Calculate the predicted value using the stored coefficients
            predicted_y = (st.session_state.b0 + 
                           st.session_state.b1 * new_x1 + 
                           st.session_state.b2 * new_x2 + 
                           st.session_state.b3 * new_x3)
            
            # Display the prediction result
            st.write(f"Predicted value for {dep_var}: {predicted_y:.4f}")
