import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="NEET-PG Counselling Care",
    page_icon="⚕️", layout="wide"
)

st.title("📊 Karnataka State Cutoff Analysis")

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
DOCS_DIR = ROOT_DIR / "Docs"

@st.cache_data
def load_state_data():
    return pd.read_csv(DOCS_DIR / "state2024cutoff.csv")

df = load_state_data()
st.write("### State Cutoff Data")

min_rank = int(df['All India Rank'].min())
max_rank = int(df['All India Rank'].max())
district_options = df['District'].unique()
category_options = df['Allotted Category'].unique()
college_options = df['Name of the College Allotted.'].unique()
course_options = df['Course Name'].unique()
round_options = df['Round'].unique()

selected_years = st.radio('Select Year : ',[2024,2023])
rank_range = st.slider('Select a Rank Range:',min_rank,max_rank,(min_rank,max_rank))
selected_districts = st.multiselect('Select one or more districts:', options=district_options)
selected_categories = st.multiselect('Select one or more Categories:', options=category_options)
selected_colleges = st.multiselect('Select the colleges:',options=college_options)
selected_courses = st.multiselect('Select the Courses:',options=course_options)
selected_rounds = st.multiselect('Select the Rounds:',options=round_options)

filtered_df = df.copy()

if selected_districts:
    filtered_df = filtered_df[filtered_df['District'].isin(selected_districts)]

if selected_categories:
    filtered_df = filtered_df[filtered_df['Allotted Category'].isin(selected_categories)]

if selected_colleges:
    filtered_df = filtered_df[filtered_df['Name of the College Allotted.'].isin(selected_colleges)]

if selected_courses:
    filtered_df = filtered_df[filtered_df['Course Name'].isin(selected_courses)]

if selected_years:
    filtered_df = filtered_df[filtered_df['Exam year'].isin([selected_years])]

if selected_rounds:
    filtered_df = filtered_df[filtered_df['Round'].isin(selected_rounds)]

filtered_df = filtered_df[(filtered_df['All India Rank']>=rank_range[0]) & (filtered_df['All India Rank']<=rank_range[1])]


st.dataframe(filtered_df)

st.download_button(label="Downlaovd Results",data=filtered_df.to_csv(),file_name="results.csv")