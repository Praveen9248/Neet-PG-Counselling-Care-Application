import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="NEET-PG Counselling Care",
    page_icon="⚕️", layout="wide"
)

st.title("🌍 All India Cutoff Analysis")

@st.cache_data
def load_all_india_data():
    filePath = os.path.join("Docs","aicutoff.csv")
    return pd.read_csv(filePath)

df = load_all_india_data()
st.write("### All India Cutoff Data")

min_rank = int(df['Rank'].min())
max_rank = int(df['Rank'].max())
state_options = df['State'].unique()
category_options = df['Candidate Category'].unique()
quota_options = df['Allotted Quota'].unique()
college_options = df['Allotted Institute'].unique()
course_options = df['Course'].unique()
round_options = df['Round'].unique()

selected_years = st.radio('Select Year : ',[2024,2023])
rank_range = st.slider('Select a Rank Range:',min_rank,max_rank,(min_rank,max_rank))
selected_states = st.multiselect('Select one or more States:', options=state_options)
selected_categories = st.multiselect('Select one or more Categories:', options=category_options)
selected_quotas = st.multiselect('Select the Quotas:',options=quota_options)
selected_colleges = st.multiselect('Select the colleges:',options=college_options)
selected_courses = st.multiselect('Select the Courses:',options=course_options)
selected_rounds = st.multiselect('Select the Rounds:',options=round_options)

filtered_df = df.copy()

if selected_states:
    filtered_df = filtered_df[filtered_df['State'].isin(selected_states)]

if selected_categories:
    filtered_df = filtered_df[filtered_df['Candidate Category'].isin(selected_categories)]

if selected_quotas:
    filtered_df = filtered_df[filtered_df['Allotted Quota'].isin(selected_quotas)]

if selected_colleges:
    filtered_df = filtered_df[filtered_df['Allotted Institute'].isin(selected_colleges)]

if selected_courses:
    filtered_df = filtered_df[filtered_df['Course'].isin(selected_courses)]

if selected_years:
    filtered_df = filtered_df[filtered_df['Exam year'].isin([selected_years])]

if selected_rounds:
    filtered_df = filtered_df[filtered_df['Round'].isin(selected_rounds)]

filtered_df = filtered_df[(filtered_df['Rank']>=rank_range[0]) & (filtered_df['Rank']<=rank_range[1])]

st.dataframe(filtered_df)

st.download_button(label="Downlaod Results",data=filtered_df.to_csv(),file_name="results.csv")