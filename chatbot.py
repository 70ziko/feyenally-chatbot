import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message

openai.api_key = st.secrets["api_secret"]