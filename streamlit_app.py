import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
#Create the app's title using st.title
st.title("🦜🔗 Quickstart App")
# Add a text input box for the user to enter their OpenAi API key.
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

#Denf a function to authenticate to OpenAI with the user's key 
def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text).content)
# Use St.form() to create text box for the user input   
with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text) 