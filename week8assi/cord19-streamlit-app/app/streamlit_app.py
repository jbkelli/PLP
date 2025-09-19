import streamlit as st
import pandas as pd
from src.data_processing import load_data, clean_data, prepare_data
from src.analysis import count_publications_by_year, top_journals
from src.visualization import plot_publications_over_time, plot_top_journals

# Set the title of the Streamlit app
st.title("CORD-19 Research Dataset Analysis")

# Load and clean the data
data = load_data()
cleaned_data = clean_data(data)
prepared_data = prepare_data(cleaned_data)

# Sidebar for user input
st.sidebar.header("User Input Features")
year = st.sidebar.selectbox("Select Year", sorted(prepared_data['year'].unique()))

# Display data based on user input
st.subheader(f"Publications in {year}")
publications_by_year = count_publications_by_year(prepared_data, year)
st.write(publications_by_year)

# Visualizations
st.subheader("Publications Over Time")
fig1 = plot_publications_over_time(prepared_data)
st.pyplot(fig1)

st.subheader("Top Journals")
top_journals_data = top_journals(prepared_data)
fig2 = plot_top_journals(top_journals_data)
st.pyplot(fig2)