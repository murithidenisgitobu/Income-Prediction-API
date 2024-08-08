import streamlit as st
import joblib
import pandas as pd

# Set up page
st.set_page_config(page_title='Income Prediction App', page_icon='📊', layout='wide')

# Set up page title
st.title('Prediction Page')

# Create form
with st.form(key='prediction_form'):
    # Define four columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.number_input('Age', min_value=0, max_value=120, value=30)
        gender = st.selectbox('Gender', options=['Male', 'Female'])
        education = st.selectbox('Education', options=[
            'High school graduate', '5th or 6th grade',
            'Bachelors degree(BA AB BS)', '9th grade', 'Children',
            'Some college but no degree', '11th grade', '10th grade',
            '7th and 8th grade', 'Associates degree-occup /vocational',
            'Masters degree(MA MS MEng MEd MSW MBA)', '12th grade no diploma',
            'Associates degree-academic program', 'Less than 1st grade',
            'Prof school degree (MD DDS DVM LLB JD)',
            '1st 2nd 3rd or 4th grade', 'Doctorate degree(PhD EdD)'
        ])
        marital_status = st.selectbox('Marital Status', options=[
            'Married-civilian spouse present', 'Never married', 'Widowed',
            'Divorced', 'Married-A F spouse present', 'Separated',
            'Married-spouse absent'
        ])
        race = st.selectbox('Race', options=[
            'White', 'Other', 'Black', 'Asian or Pacific Islander',
            'Amer Indian Aleut or Eskimo'
        ])
        is_hispanic = st.selectbox('Hispanic', options=[
            'All other', 'Central or South American', 'Puerto Rican',
            'Mexican (Mexicano)', 'Mexican-American', 'Chicano', 'Other Spanish',
            'NA', 'Cuban', 'Do not know'
        ])
        employment_commitment = st.selectbox('Employment Commitment', options=[
            'Children or Armed Forces', 'Full-time schedules', 'Not in labor force',
            'PT for non-econ reasons usually FT', 'Unemployed full-time',
            'PT for econ reasons usually PT', 'Unemployed part- time',
            'PT for econ reasons usually FT'
        ])
        
    with col2:
        wage_per_hour = st.number_input('Wage per Hour', min_value=0.0, format="%.2f")
        working_week_per_year = st.number_input('Working Weeks per Year', min_value=0, max_value=52, value=40)
        industry_code = st.selectbox('Industry Code', options=[
            29, 5, 37, 0, 34, 31, 32, 43, 25, 8, 44, 33, 49, 42, 39, 45, 30, 22, 19, 41,
            4, 47, 1, 35, 2, 24, 40, 38, 48, 15, 16, 11, 27, 13, 50, 9, 23, 14, 36, 12,
            51, 18, 28, 3, 21, 7, 6, 46, 17, 26, 20, 10
        ])
        industry_code_main = st.selectbox('Main Industry Code', options=[
            'Transportation', 'Manufacturing-durable goods',
            'Business and repair services', 'Not in universe or children',
            'Finance insurance and real estate', 'Utilities and sanitary services',
            'Wholesale trade', 'Education', 'Manufacturing-nondurable goods',
            'Social services', 'Retail trade', 'Public administration',
            'Medical except hospital', 'Personal services except private HH',
            'Other professional services', 'Communications', 'Hospital services',
            'Construction', 'Agriculture', 'Entertainment', 'Private household services',
            'Armed Forces', 'Mining', 'Forestry and fisheries'
        ])
        occupation_code = st.selectbox('Occupation Code', options=[
            38, 37, 4, 0, 26, 34, 25, 12, 14, 3, 41, 30, 29, 19, 2, 36, 35, 28, 7, 31,
            8, 32, 24, 10, 16, 23, 33, 43, 17, 13, 44, 42, 5, 40, 18, 27, 39, 46, 11, 9,
            22, 1, 21, 15, 6, 45, 20
        ])
        total_employed = st.number_input('Total Employed', min_value=0)
        household_stat = st.selectbox('Household Status', options=[
            'Householder', 'Child <18 never marr not in subfamily',
            'Nonfamily householder', 'Child 18+ never marr Not in a subfamily',
            'Spouse of householder', 'Child 18+ never marr RP of subfamily',
            'Other Rel 18+ never marr not in subfamily',
            'Grandchild <18 never marr not in subfamily',
            'Child 18+ ever marr RP of subfamily',
            'Other Rel <18 never marr not in subfamily',
            'Grandchild <18 never marr child of subfamily RP', 'Secondary individual',
            'Grandchild 18+ never marr not in subfamily',
            'Other Rel 18+ ever marr not in subfamily',
            'Other Rel <18 never marr child of subfamily RP',
            'RP of unrelated subfamily', 'Child 18+ ever marr Not in a subfamily',
            'Other Rel 18+ ever marr RP of subfamily',
            'Other Rel <18 spouse of subfamily RP',
            'Child under 18 of RP of unrel subfamily', 'In group quarters',
            'Child <18 never marr RP of subfamily',
            'Grandchild 18+ ever marr not in subfamily',
            'Other Rel 18+ never marr RP of subfamily',
            'Child 18+ spouse of subfamily RP',
            'Other Rel <18 never marr RP of subfamily',
            'Child <18 ever marr not in subfamily',
            'Spouse of RP of unrelated subfamily',
            'Grandchild 18+ never marr RP of subfamily',
            'Grandchild 18+ ever marr RP of subfamily',
            'Grandchild <18 never marr RP of subfamily',
            'Child <18 ever marr RP of subfamily',
            'Other Rel <18 ever marr RP of subfamily',
            'Other Rel <18 spouse of subfamily RP', 'Child <18 spouse of subfamily RP'
        ])

    with col3:
        household_summary = st.selectbox('Household Summary', options=[
            'Householder', 'Child under 18 never married', 'Child 18 or older',
            'Spouse of householder', 'Other relative of householder',
            'Nonrelative of householder', 'Group Quarters- Secondary individual',
            'Child under 18 ever married'
        ])
        vet_benefit = st.selectbox('Veteran Benefits', options=['Yes', 'No'])
        tax_status = st.selectbox('Tax Status', options=[
            'Joint both under 65', 'Single', 'Nonfiler', 'Head of household',
            'Joint one under 65 & one 65+', 'Joint both 65+'
        ])
        gains = st.number_input('Gains', min_value=0.0, format="%.2f")
        losses = st.number_input('Losses', min_value=0.0, format="%.2f")
        stocks_status = st.selectbox('Stocks Status', options=['Own', 'Do Not Own'])
        citizenship = st.selectbox('Citizenship', options=[
            'Native', 'Foreign born- Not a citizen of U S',
            'Native- Born in Puerto Rico or U S Outlying',
            'Foreign born- U S citizen by naturalization',
            'Native- Born abroad of American Parent(s)'
        ])

    with col4:
        mig_year = st.number_input('Years in Current MSA', min_value=0)
        country_of_birth_own = st.selectbox('Country of Birth (Own)', options=[
            'US', 'El-Salvador', 'Cuba', 'Honduras', 'Nicaragua', 'Guatemala', 'Other Central America',
            'Other South America', 'Colombia', 'Peru', 'Ecuador', 'Venezuela', 'Brazil',
            'Other Latin America', 'Other North America', 'Mexico', 'Other South America',
            'Country of Birth unknown'
        ])
        country_of_birth_mother = st.selectbox('Country of Birth Mother', options=[
            'US', 'Other Central America', 'Mexico', 'Other South America', 'Guatemala',
            'Other North America', 'Honduras', 'El-Salvador', 'Other Latin America',
            'Other Caribbean', 'Cuba', 'Country of Birth unknown'
        ])
        country_of_birth_father = st.selectbox('Country of Birth Father', options=[
            'US', 'Mexico', 'Other Central America', 'Other South America', 'Guatemala',
            'Other North America', 'Honduras', 'Other Latin America', 'El-Salvador',
            'Other Caribbean', 'Cuba', 'Country of Birth unknown'
        ])
        importance_of_record = st.selectbox('Importance of Record', options=[
            'Slightly important', 'Important', 'Not important', 'Very important', 'Extremely important'
        ])
        employment_stat = st.selectbox('Employment Status', options=[
            'Employed', 'Unemployed', 'Not in labor force'
        ])

    # Submit button
    submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        # Create input DataFrame
        input_data = pd.DataFrame({
            'age': [age],
            'gender': [gender],
            'education': [education],
            'marital_status': [marital_status],
            'race': [race],
            'is_hispanic': [is_hispanic],
            'employment_commitment': [employment_commitment],
            'wage_per_hour': [wage_per_hour],
            'working_week_per_year': [working_week_per_year],
            'industry_code': [industry_code],
            'industry_code_main': [industry_code_main],
            'occupation_code': [occupation_code],
            'total_employed': [total_employed],
            'household_stat': [household_stat],
            'household_summary': [household_summary],
            'vet_benefit': [vet_benefit],
            'tax_status': [tax_status],
            'gains': [gains],
            'losses': [losses],
            'stocks_status': [stocks_status],
            'citizenship': [citizenship],
            'mig_year': [mig_year],
            'country_of_birth_own': [country_of_birth_own],
            'country_of_birth_mother': [country_of_birth_mother],
            'country_of_birth_father': [country_of_birth_father],
            'importance_of_record': [importance_of_record],
            'employment_stat': [employment_stat]
        })

        # Load the selected model
        model_choice = st.selectbox('Select Model', options=['Random Forest', 'XGBoost'])
        if model_choice == 'Random Forest':
            model = joblib.load(r'toolkit\rf_model.joblib')
        elif model_choice == 'XGBoost':
            model = joblib.load(r'toolkit\xgb_model.joblib')

        # Make prediction
        try:
            prediction = model.predict(input_data)
            st.write(f'Prediction: {prediction[0]}')
        except Exception as e:
            st.error(f'Error during prediction: {e}')
