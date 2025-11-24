import joblib
import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(page_title="LPA Predictor", page_icon="🔥", layout="centered")

# Title and header
st.title("Check LPA 🔥")
st.header("Check your LPA with respect to your CGPA")

# Load the model
filename = "linear.joblib"
try:
    loaded_model = joblib.load(filename=filename)
    st.success("✅ Model is loaded successfully!")
except FileNotFoundError:
    st.error("❌ Model file not found! Please ensure 'linear.joblib' is in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading model: {str(e)}")
    st.stop()

# Display model information
with st.expander("ℹ️ Model Information"):
    st.write(f"**Model Type:** Linear Regression")
    st.write(f"**Intercept:** {loaded_model.intercept_:.4f}")
    st.write(f"**Coefficient:** {loaded_model.coef_[0]:.4f}")
    st.write(f"**Equation:** LPA = {loaded_model.coef_[0]:.4f} × CGPA + {loaded_model.intercept_:.4f}")

# Create input section
st.markdown("---")
st.subheader("📊 Enter Your Details")

# CGPA input with validation
cgpa_input = st.number_input(
    "Enter Your CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.01,
    format="%.2f",
    help="Enter your CGPA (0.0 to 10.0)"
)

# Display the input value
st.info(f"Your CGPA: **{cgpa_input:.2f}**")

# Predict button
btn = st.button("🔮 Predict LPA", type="primary", use_container_width=True)

if btn:
    if cgpa_input <= 0:
        st.warning("⚠️ Please enter a valid CGPA greater than 0")
    else:
        # Reshape input for prediction (model expects 2D array)
        cgpa_array = np.array([[cgpa_input]])
        cgpa_array 
        
        
        # Make prediction
        predicted_lpa = loaded_model.predict(cgpa_array)[0]
        
        # Display results
        st.markdown("---")
        st.subheader("🎯 Prediction Results")
        
        # Display prediction in a nice card
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                label="Your CGPA",
                value=f"{cgpa_input:.2f}",
                delta=None
            )
        
        with col2:
            st.metric(
                label="Predicted LPA",
                value=f"₹{predicted_lpa:.2f} L",
                delta=None
            )
        
        # Success message with detailed info
        if predicted_lpa > 0:
            st.success(f"✅ Your predicted LPA is: **₹{predicted_lpa:.2f} Lakhs per annum**")
            
            # Additional insights
            st.markdown("---")
            st.subheader("📈 Additional Insights")
            
            # Calculate range (assuming some variance)
            lower_bound = max(0, predicted_lpa - 0.5)
            upper_bound = predicted_lpa + 0.5
            
            st.info(f"""
            - **Expected Range:** ₹{lower_bound:.2f}L - ₹{upper_bound:.2f}L
            - **Based on CGPA:** {cgpa_input:.2f}/10.0
            - This prediction is based on historical placement data
            """)
        else:
            st.warning("⚠️ The predicted LPA is negative or zero. This might indicate that your CGPA is below the minimum placement threshold.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with ❤️ using Streamlit | Data-driven placement predictions</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with additional information
with st.sidebar:
    st.header("📖 About")
    st.write("""
    This application predicts your expected LPA (Lakhs Per Annum) 
    based on your CGPA using a Linear Regression model trained on 
    historical placement data.
    """)
    
    st.header("📋 Instructions")
    st.write("""
    1. Enter your CGPA (0.0 to 10.0)
    2. Click on 'Predict LPA'
    3. View your predicted salary package
    """)
    
    st.header("⚠️ Disclaimer")
    st.write("""
    This is a prediction based on historical data. Actual placement 
    packages may vary based on multiple factors including market 
    conditions, company policies, and individual performance.
    """)