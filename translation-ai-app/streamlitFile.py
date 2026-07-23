import streamlit as st
import requests

st.set_page_config(page_title="Translate", page_icon="🤖")
st.title("Translate")
st.markdown("---")

user_text = st.text_input("input your text:")

provider =st.selectbox(
    "Choose LLM",
    ["ollama","huggingface"]
)

if st.button("Translate"):
    if user_text:
        response = requests.post(
            "http://localhost:8000/translate",
            json={
                "text": user_text,
                "provider":provider
                }
        )
        st.write(response.json())

    else:
        st.warning("please enter text")
                    
