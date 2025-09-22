import streamlit as st
# Set page configuration, including a title and an icon.
st.set_page_config(
    page_title="NEET-PG Counselling Care",
    page_icon="⚕️", layout="wide"
)

# --- Title and Introduction ---
st.title("NEET-PG Counselling Care: Your Trusted Guide 🩺")
col1, col2= st.columns(2)
with col1:
    st.image("assets/banner.png",width=400)

with col2:
    st.markdown("""
        #### Navigating the path to your dream residency.
    """)
    st.write(
        "Welcome to the ultimate resource for NEET-PG aspirants. We understand that the "
        "counselling process can be complex and overwhelming. Our mission is to simplify "
        "your journey by providing accurate, data-driven insights and personalized guidance."
    )

# --- Problem and Solution Section ---
st.header("The Challenge of Counselling")
st.write(
    "Every year, thousands of students face the daunting task of analyzing vast amounts of data "
    "to make the right choices for their medical residency. Sifting through cutoff PDFs, "
    "comparing ranks, and understanding historical trends is a time-consuming process. "
    "Small mistakes can have a significant impact on your future."
)

# --- Features Section (using columns for a clean look) ---
st.header("How We Help You Succeed")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Data-Driven Analysis")
    st.write(
        "Access comprehensive cutoff data from both All India Quota and Karnataka State, "
        "for 2024 and 2023. Our platform consolidates and organizes this critical "
        "information so you don't have to."
    )
    
with col2:
    st.subheader("🤖 AI-Powered Guidance")
    st.write(
        "Our intelligent AI assistant provides personalized advice and answers your specific "
        "questions, helping you make informed decisions based on your rank, category, and preferences."
    )
    
with col3:
    st.subheader("📈 Interactive Visualizations")
    st.write(
        "Go beyond raw numbers. Our visualization tools allow you to explore trends, "
        "compare different years, and gain a deeper understanding of the cutoff landscape at a glance."
    )

st.header("About This Project")
st.write(
    "This project was born out of a desire to empower medical aspirants with the "
    "tools they need to succeed. By meticulously collecting and analyzing past cutoff "
    "data, we aim to eliminate guesswork and provide a clear, data-driven path to "
    "your medical residency goals. We believe that with the right information, "
    "you can make the best decision for your future."
)

# --- Call to Action ---
st.subheader("Ready to Get Started?")
st.write(
    "Navigate using the menu on the left to explore all the features we have to offer. "
    "Whether you're looking for specific college cutoffs or need personalized AI help, "
    "we've got you covered."
)
