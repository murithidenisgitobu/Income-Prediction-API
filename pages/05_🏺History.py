import streamlit as st
import pandas as pd

# Set up page configuration
st.set_page_config(page_title='History Page', page_icon='🏺', layout='wide')

# Set up page title
st.title('History Page')

# Load data
@st.cache_data(show_spinner='Loading data ...')
def load_data():
    df = pd.read_csv('Data/history.csv')
    return df

# Load the history data
df = load_data()

# Display the data
st.write(df)

# Convert the history data to CSV
csv_data = df.to_csv(index=False).encode('utf-8')

# Add download button for the history file
st.download_button(
    label="Download History as CSV",
    data=csv_data,
    file_name="history.csv",
    mime="text/csv",
)
