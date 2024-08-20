
# Income Prediction Challenge for Azubian

The objective of this project is to develop a machine learning model to predict whether an individual earns above or below a certain income threshold. This tool aims to assist policymakers in monitoring income levels, managing income inequality, and addressing challenges posed by AI and automation.

## Features

The dataset used in this project contains 43 columns and 209,499 rows. The features are as follows:

- **ID**: Unique identifier for each individual.
- **age**: Age of the individual.
- **gender**: Gender of the individual.
- **education**: Level of education of the individual.
- **class**: Social class of the individual.
- **education_institute**: Type of educational institution attended.
- **marital_status**: Marital status of the individual.
- **race**: Race of the individual.
- **is_hispanic**: Indicator for Hispanic ethnicity.
- **employment_commitment**: Level of commitment to employment.
- **unemployment_reason**: Reason for unemployment.
- **employment_stat**: Employment status of the individual.
- **wage_per_hour**: Hourly wage of the individual.
- **is_labor_union**: Membership in a labor union.
- **working_week_per_year**: Number of weeks worked per year.
- **industry_code**: Code representing the industry of employment.
- **industry_code_main**: Main industry code.
- **occupation_code**: Code representing the occupation.
- **occupation_code_main**: Main occupation code.
- **total_employed**: Total number of individuals employed.
- **household_stat**: Household status.
- **household_summary**: Summary of household information.
- **under_18_family**: Presence of individuals under 18 in the family.
- **veterans_admin_questionnaire**: Veteran status questionnaire.
- **vet_benefit**: Veteran benefits received.
- **tax_status**: Tax status of the individual.
- **gains**: Financial gains.
- **losses**: Financial losses.
- **stocks_status**: Status of stocks owned.
- **citizenship**: Citizenship status.
- **mig_year**: Year of migration.
- **country_of_birth_own**: Country of birth of the individual.
- **country_of_birth_father**: Country of birth of the individual's father.
- **country_of_birth_mother**: Country of birth of the individual's mother.
- **migration_code_change_in_msa**: Code for change in MSA migration.
- **migration_prev_sunbelt**: Previous migration status in the Sunbelt.
- **migration_code_move_within_reg**: Code for moving within a region.
- **migration_code_change_in_reg**: Code for change in region migration.
- **residence_1_year_ago**: Previous residence status.
- **old_residence_reg**: Previous residence region.
- **old_residence_state**: Previous residence state.
- **importance_of_record**: Importance of the record.
- **income_above_limit**: Indicator for income above a certain limit.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/murithidenisgitobu/Income-Prediction-API
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Navigate to the Project Directory**
    ```bash
    cd api
    ```

4. **Start the Server**
    ```bash
    uvicorn app:app --reload
    ```

## Running the Streamlit App

To run the Streamlit app, use the following command:

```bash
streamlit run Home.py

## Screenshots

## App Screenshots
![image](https://github.com/user-attachments/assets/6c9423ec-e640-47df-b13f-f2d4b8cebd48)

## API screshot
![image](https://github.com/user-attachments/assets/b6d63ee4-c3a9-4ec3-a7a8-bffc020b5af2)


## Power Point Link

https://1drv.ms/p/s!AveoYC37sJ-ygWaHGKoZuFnoCioR
