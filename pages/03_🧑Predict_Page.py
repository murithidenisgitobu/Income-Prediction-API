import streamlit as st
import joblib
import pandas as pd

# Set up page
st.set_page_config(page_title='Income Prediction App', page_icon='📊', layout='wide')

# Set up page title
st.title('Prediction Page')

# Load models and encoder
with st.spinner('Loading models and encoder...'):
    model_forest = joblib.load(r'toolkit\rf_model.joblib')
    model_xgb = joblib.load(r'toolkit\xgb_model.joblib')
    encoder = joblib.load(r'toolkit\label_encoder.joblib')

# Choose Model to Use
model_choice = st.selectbox('Choose Model', options=['Random Forest', 'XGBoost'])

# Create form
with st.form(key='prediction_form'):
    # Define four columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.number_input('Age', min_value=0, max_value=90, value=30)
        gender = st.selectbox('Gender', options=['Female', 'Male'])
        education = st.selectbox('Education', options=[
            'High school graduate', '12th grade no diploma', 'Children',
            'Bachelors degree(BA AB BS)', '7th and 8th grade', '11th grade', '9th grade',
            'Masters degree(MA MS MEng MEd MSW MBA)', '10th grade',
            'Associates degree-academic program', '1st 2nd 3rd or 4th grade',
            'Some college but no degree', 'Less than 1st grade',
            'Associates degree-occup /vocational',
            'Prof school degree (MD DDS DVM LLB JD)', '5th or 6th grade',
            'Doctorate degree(PhD EdD)'
        ])
        marital_status = st.selectbox('Marital Status', options=[
            'Widowed', 'Never married', 'Married-civilian spouse present', 'Divorced',
            'Married-spouse absent', 'Separated', 'Married-A F spouse present'
        ])
        race = st.selectbox('Race', options=[
            'White', 'Black', 'Asian or Pacific Islander', 'Amer Indian Aleut or Eskimo',
            'Other'
        ])
        is_hispanic = st.selectbox('Hispanic', options=[
            'All other', 'Mexican-American', 'Central or South American',
            'Mexican (Mexicano)', 'Puerto Rican', 'Other Spanish', 'Cuban', 'Do not know',
            'Chicano'
        ])
        employment_commitment = st.selectbox('Employment Commitment', options=[
            'Not in labor force', 'Children or Armed Forces', 'Full-time schedules',
            'PT for econ reasons usually PT', 'Unemployed full-time',
            'PT for non-econ reasons usually FT', 'PT for econ reasons usually FT',
            'Unemployed part- time'
        ])
        
    with col2:
        employment_stat = st.selectbox('Employment Status', options=[0, 1, 2])
        wage_per_hour = st.number_input('Wage per Hour', min_value=0, max_value=1949)
        working_week_per_year = st.number_input('Working Weeks per Year', min_value=0, max_value=52, value=40)
        industry_code = st.selectbox('Industry Code', options=list(range(52)))
        industry_code_main = st.selectbox('Main Industry Code', options=[
            'Not in universe or children', 'Hospital services', 'Retail trade',
            'Finance insurance and real estate', 'Manufacturing-nondurable goods',
            'Transportation', 'Business and repair services', 'Medical except hospital',
            'Education', 'Construction', 'Manufacturing-durable goods',
            'Public administration', 'Agriculture', 'Other professional services',
            'Mining', 'Utilities and sanitary services', 'Private household services',
            'Personal services except private HH', 'Wholesale trade', 'Communications',
            'Entertainment', 'Social services', 'Forestry and fisheries', 'Armed Forces'
        ])
       
        total_employed = st.selectbox('Total Employed', options=[0, 1, 2, 3, 4, 5, 6])
        household_stat = st.selectbox('Household Status', options=[
            'Householder', 'Nonfamily householder',
            'Child 18+ never marr Not in a subfamily',
            'Child <18 never marr not in subfamily', 'Spouse of householder',
            'Child 18+ spouse of subfamily RP', 'Secondary individual',
            'Child 18+ never marr RP of subfamily',
            'Other Rel 18+ spouse of subfamily RP',
            'Grandchild <18 never marr not in subfamily',
            'Other Rel <18 never marr child of subfamily RP',
            'Other Rel 18+ ever marr RP of subfamily',
            'Other Rel 18+ ever marr not in subfamily',
            'Child 18+ ever marr Not in a subfamily', 'RP of unrelated subfamily',
            'Child 18+ ever marr RP of subfamily',
            'Other Rel 18+ never marr not in subfamily',
            'Child under 18 of RP of unrel subfamily',
            'Grandchild <18 never marr child of subfamily RP',
            'Grandchild 18+ never marr not in subfamily',
            'Other Rel <18 never marr not in subfamily', 'In group quarters',
            'Grandchild 18+ ever marr not in subfamily',
            'Other Rel 18+ never marr RP of subfamily',
            'Child <18 never marr RP of subfamily',
            'Grandchild 18+ never marr RP of subfamily',
            'Spouse of RP of unrelated subfamily',
            'Grandchild 18+ ever marr RP of subfamily',
            'Child <18 ever marr not in subfamily',
            'Child <18 ever marr RP of subfamily',
            'Other Rel <18 ever marr RP of subfamily',
            'Grandchild 18+ spouse of subfamily RP',
            'Child <18 spouse of subfamily RP',
            'Other Rel <18 ever marr not in subfamily',
            'Other Rel <18 never married RP of subfamily',
            'Other Rel <18 spouse of subfamily RP',
            'Grandchild <18 ever marr not in subfamily',
            'Grandchild <18 never marr RP of subfamily'
        ])

    with col3:
        household_summary = st.selectbox('Household Summary', options=[
            'Householder', 'Child 18 or older', 'Child under 18 never married',
            'Spouse of householder', 'Nonrelative of householder',
            'Other relative of householder', 'Group Quarters- Secondary individual',
            'Child under 18 ever married'
        ])
        vet_benefit = st.selectbox('Veteran Benefits', options=[0, 1, 2])
        tax_status = st.selectbox('Tax Status', options=[
            'Head of household', 'Single', 'Nonfiler', 'Joint both 65+',
            'Joint both under 65', 'Joint one under 65 & one 65+'
        ])
        gains = st.number_input('Gains', min_value=0, max_value=99999)
        losses = st.number_input('Losses', min_value=0, max_value=4608)
        stocks_status = st.number_input('Stocks Status', min_value=0, max_value=5531, step=1)
        citizenship = st.selectbox('Citizenship', options=[
            'Native', 'Foreign born- Not a citizen of U S',
            'Foreign born- U S citizen by naturalization',
            'Native- Born abroad of American Parent(s)',
            'Native- Born in Puerto Rico or U S Outlying'
        ])

    with col4:
        mig_year = st.selectbox('Migration Year', options=[94, 95])
        country_of_birth_own = st.selectbox('Country of Birth (Own)', options=[
            'US', 'El-Salvador', 'Mexico', 'Philippines', 'Cambodia', 'China',
            'Hungary', 'Puerto-Rico', 'England', 'Dominican-Republic', 'Japan', 'Canada',
            'Ecuador', 'Italy', 'Cuba', 'Peru', 'Taiwan', 'South Korea', 'Poland',
            'Nicaragua', 'Germany', 'Guatemala', 'India', 'Ireland', 'Honduras', 'France',
            'Trinadad&Tobago', 'Thailand', 'Iran', 'Vietnam', 'Portugal', 'Laos', 'Panama',
            'Scotland', 'Columbia', 'Jamaica', 'Greece', 'Haiti', 'Yugoslavia',
            'Outlying-U S (Guam USVI etc)', 'Holand-Netherlands', 'Hong Kong'
        ])
        country_of_birth_mother = st.selectbox('Country of Birth Mother', options=[
            'US', 'India', 'Peru', 'Germany', 'El-Salvador', 'Mexico', 'Puerto-Rico',
            'Philippines', 'Canada', 'France', 'Cambodia', 'Italy', 'Ecuador', 'China',
            'Hungary', 'Dominican-Republic', 'Japan', 'England', 'Cuba', 'Poland',
            'South Korea', 'Yugoslavia', 'Scotland', 'Nicaragua', 'Guatemala',
            'Holand-Netherlands', 'Greece', 'Ireland', 'Honduras', 'Haiti',
            'Outlying-U S (Guam USVI etc)', 'Trinadad&Tobago', 'Thailand', 'Jamaica',
            'Iran', 'Vietnam', 'Columbia', 'Portugal', 'Laos', 'Taiwan', 'Hong Kong',
            'Panama'
        ])
        country_of_birth_father = st.selectbox('Country of Birth Father', options=[
            'US', 'India', 'Poland', 'Germany', 'El-Salvador', 'Mexico', 'Puerto-Rico',
            'Philippines', 'Greece', 'Canada', 'Ireland', 'Cambodia', 'Ecuador', 'China',
            'Hungary', 'Dominican-Republic', 'Japan', 'Italy', 'Cuba', 'Peru', 'Jamaica',
            'South Korea', 'Yugoslavia', 'Nicaragua', 'Columbia', 'Guatemala', 'France',
            'England', 'Iran', 'Honduras', 'Haiti', 'Trinadad&Tobago',
            'Outlying-U S (Guam USVI etc)', 'Thailand', 'Vietnam', 'Hong Kong',
            'Portugal', 'Laos', 'Scotland', 'Taiwan', 'Holand-Netherlands', 'Panama'
        ])
        importance_of_record = st.number_input('Importance of Record', min_value=0.0, max_value=2366.75, format="%.2f")

        occupation_code = st.selectbox('Occupation Code', options=[
            38, 37, 4, 0, 26, 34, 25, 12, 14, 3, 41, 30, 29, 19, 2, 36, 35, 28, 7, 31,
            8, 32, 24, 10, 16, 23, 33, 43, 17, 13, 44, 42, 5, 40, 18, 27, 39, 46, 11, 9,
            22, 1, 21, 15, 6, 45, 20
        ])

    submit_button = st.form_submit_button('Submit')

# Make predictions
if submit_button:
    # Prepare data for prediction
    data = pd.DataFrame({
        'age': [age],
        'gender': [gender],
        'education': [education],
        'marital_status': [marital_status],
        'race': [race],
        'is_hispanic': [is_hispanic],
        'employment_commitment': [employment_commitment],
        'employment_stat': [employment_stat],
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
        'importance_of_record': [importance_of_record]
    })

    if model_choice == 'Random Forest':
        prediction = model_forest.predict(data)
    else:
        prediction = model_xgb.predict(data)

    # Inverse transform the predictions to get the original categorical values
    original_prediction = encoder.inverse_transform(prediction)

    # Display results
    st.write(f'{model_choice} Prediction: {original_prediction[0]}')