import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

# Read your HTML file
with open("AI_Resume_Matcher_Enhanced.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display it in the app
components.html(html_code, height=1000, scrolling=True)