import openai
import streamlit as st
import os

# Read environment variables from local .env file
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(_file_), '.env')
load_dotenv(dotenv_path)

if "messages" not in st.session_state:
    st.session_state.messages = []
    
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") or "Add your open API key here"

# Set OpenAI API details
openai.api_key = OPENAI_API_KEY

system_prompt = f"  Write whole code"

def ask_gpt(message):
    message_series = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_series,
        temperature=0.1,
    )

    response_string = response['choices'][0]['message']['content']

    return response_string

# st.session_state = st.empty()

with st.sidebar:
    "So Secure"

st.title("Dense net code")

if "current_level" not in st.session_state:
    st.session_state["current_level"] = THIS_LEVEL
else:
    if st.session_state["current_level"] is not THIS_LEVEL:
        del st.session_state["messages"]
        st.session_state["current_level"] = THIS_LEVEL

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": ""}]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = ask_gpt(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
