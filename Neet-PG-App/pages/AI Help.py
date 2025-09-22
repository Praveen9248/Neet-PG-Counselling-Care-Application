import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(
    page_title="NEET-PG Counselling Care",
    page_icon="⚕️", layout="wide"
)

# 🔑 Access API key from secrets
api_key = st.secrets["api_keys"]["google"]

if api_key:
    genai.configure(api_key=api_key)
   
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
else:
    st.error("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    model = None

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Gemini AI Chatbot")
st.markdown("Ask me anything! I am a large language model trained by Google.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if model:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            chat_history = []
            for message in st.session_state.messages:
                role = "user" if message["role"] == "user" else "model"
                chat_history.append({"role": role, "parts": [{"text": message["content"]}]})

            chat_session = model.start_chat(history=chat_history)
            
            try:
                for chunk in chat_session.send_message(prompt, stream=True):
                    full_response += chunk.text
                    time.sleep(0.05)
                    message_placeholder.markdown(full_response + "▌")
            except genai.APIError as e:
                full_response = f"An API error occurred: {e}"
            except Exception as e:
                full_response = f"An unexpected error occurred: {e}"
            
            message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})
