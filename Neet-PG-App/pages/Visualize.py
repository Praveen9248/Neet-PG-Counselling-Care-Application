import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "Docs"

def load_data():
    @st.cache_data
    def get_data():
        df = pd.read_csv(DOCS_DIR / "aicutoff.csv")
        df.columns = df.columns.str.strip()
        df = df.rename(columns={'Allotted Institute': 'Allotted_Institute', 'Exam year': 'Exam_year', 'Allotted Quota': 'Allotted_Quota', 'Round': 'Round'})
        return df

    return get_data()


st.set_page_config(
page_title="NEET-PG Counselling Care",
page_icon="⚕️", layout="wide")

st.title("Interactive Counselling Data Visualizations")

df = load_data()

years = sorted(df['Exam_year'].unique(), reverse=True)
allotted_institutes = (df['Allotted_Institute'].unique())

st.header("Select Your Filters")

selected_year = st.selectbox("Choose Exam Year:", years)
selected_college = st.selectbox("Choose a College:", allotted_institutes)

filtered_df = df[
    (df['Exam_year'] == selected_year) & 
    (df['Allotted_Institute'] == selected_college)
]

if filtered_df.empty:
    st.warning(f"No data available for {selected_college} in {selected_year}. Please select a different college or year.")

st.header(f"Insights for {selected_college} in {selected_year}")


st.subheader("Cutoff Ranks by Course and Round")

fig_bar = px.bar(
    filtered_df,
    x="Course",
    y="Rank",
    color="Round",
    title=f"Course-wise Cutoff Ranks for {selected_college}",
    hover_data=["Candidate Category", "Allotted_Quota"],
    labels={"Rank": "Closing Rank", "Course": "Medical Course"}
)
st.plotly_chart(fig_bar, use_container_width=True)
st.markdown("This chart helps you see the closing ranks for each course and how they changed across different counselling rounds.")

st.subheader("Closing Rank Trends Over Rounds")

filtered_df['Round_Order'] = filtered_df['Round'].astype('category').cat.set_categories(['Round 1', 'Round 2', 'Round 3', 'Stray Vacancy'], ordered=True)

chart_data = filtered_df.sort_values('Round_Order')

line_chart = alt.Chart(chart_data).mark_line(point=True).encode(
    x=alt.X('Round', sort=['Round 1', 'Round 2', 'Round 3', 'Stray Vacancy'], axis=alt.Axis(title='Counselling Round')),
    y=alt.Y('Rank', title='Closing Rank'),
    color='Course',
    tooltip=['Course', 'Rank', 'Allotted_Quota', 'Candidate Category']
).properties(
    title=f"Closing Rank Trends for {selected_college}"
).interactive()

st.altair_chart(line_chart, use_container_width=True)
st.markdown("This visualization shows the rank movement for various courses across different rounds, giving you a clear picture of the trend.")

st.subheader("Opening and Closing Ranks by Course and Category")

summary_df = filtered_df.groupby(['Course', 'Candidate Category']).agg(
    opening_rank=('Rank', 'min'),
    closing_rank=('Rank', 'max')
).reset_index()

summary_df.insert(0, 'Allotted Institute', selected_college)

st.dataframe(summary_df, use_container_width=True)
st.markdown("This table summarizes the opening and closing ranks for each course and category at the selected college.")

filtered_df_two = filtered_df.copy()
st.subheader("Rank Distribution by Course (Box Plot)")
categories = sorted(filtered_df['Candidate Category'].unique())
selected_category = st.selectbox("Choose a Candidate Category:", categories)
if selected_category:
    filtered_df_two = filtered_df_two[filtered_df_two['Candidate Category'].isin([selected_category])]

fig_box = px.box(
    filtered_df_two,
    x="Course",
    y="Rank",
    points="all",
    title=f"Distribution of Ranks for {selected_college}, {selected_category}",
    labels={"Rank": "Rank", "Course": "Medical Course"}
)
st.plotly_chart(fig_box, use_container_width=True)
st.markdown("The box plot gives you a clear view of the rank distribution, including the median, quartiles, and any outliers. This helps you understand the overall range of ranks for a course, not just the opening and closing values.The median value provides the most probable closing ranks avoiding sudden jumps in ranks cutoff.")