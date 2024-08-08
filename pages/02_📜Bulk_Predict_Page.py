import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title='Predict Page', page_icon='📜', layout='wide')

# Set up page title
st.title('Prediction Page')

# Load models
@st.cache_resource(show_spinner='Models Loading ...')
def load_models():
    xgb = joblib.load(r'toolkit\xgb_model.joblib')
    rfc = joblib.load(r'toolkit\rf_model.joblib')
    encoder = joblib.load(r'toolkit\label_encoder.joblib')
    return xgb, rfc, encoder

# Load the models
xgb_model, rfc_model, label_encoder = load_models()

# Prediction function
def predict_bulk(model, data):
    predictions = model.predict(data)
    probabilities = model.predict_proba(data)[:, 1]  # Probabilities for the positive class
    return predictions, probabilities

# Data cleaning function
def clean_data(data):
    # Preserve ID column and drop other columns
    if 'ID' in data.columns:
        ids = data['ID']
    else:
        ids = pd.Series(range(len(data)))
    # Columns to drop
    columns_to_drop = [
        'class', 'education_institute', 'unemployment_reason', 'is_labor_union',
        'occupation_code_main', 'under_18_family', 'veterans_admin_questionnaire', 
        'migration_prev_sunbelt', 'migration_code_move_within_reg',
        'migration_code_change_in_reg', 'residence_1_year_ago', 'old_residence_reg',
        'old_residence_state'
    ]

    data = data.drop(columns=columns_to_drop, errors='ignore')

    # Select only categorical columns
    cat_cols = data.select_dtypes(exclude=['number', 'float']).columns

    # Strip leading and trailing spaces in all categorical columns
    data[cat_cols] = data[cat_cols].applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Replace '?' with NaN in specific columns
    columns_to_strip = data.columns

    for column in columns_to_strip:
        if column in data.columns:
            data[column] = data[column].replace('?', np.nan)

    # Replace 'NA' with 'All other' in 'is_hispanic' column
    if 'is_hispanic' in data.columns:
        data['is_hispanic'] = data['is_hispanic'].replace('NA', 'All other')

    return data, ids

# User upload file section
st.subheader('Upload your CSV file for prediction')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Read the uploaded file
    user_data = pd.read_csv(uploaded_file)
    
    # Clean the data and keep ID if present
    cleaned_data, ids = clean_data(user_data)
    
    # Display cleaned data
    st.subheader('Data Loaded for Prediction')
    st.write(cleaned_data)

    # Select model for prediction
    model_choice = st.selectbox('Choose a model for prediction', ('XGBoost', 'Random Forest'))
    model = xgb_model if model_choice == 'XGBoost' else rfc_model

    # Make predictions
    predictions, probabilities = predict_bulk(model, cleaned_data)

    # Inverse encoding for predictions
    predictions = label_encoder.inverse_transform(predictions)

    # Prepare results DataFrame
    results_df = pd.DataFrame({
        'ID': ids,
        'Prediction': predictions,
        'Probability': probabilities
    })

    # Display results
    st.subheader('Prediction Results')
    st.write(results_df)

    # Filter options
    filter_option = st.selectbox('Filter results by prediction', ['Show All', 'Above limit', 'Below limit'])
    
    if filter_option != 'Show All':
        filtered_results = results_df[results_df['Prediction'] == filter_option]
        st.subheader(f'Results Filtered by {filter_option}')
        st.write(filtered_results)
