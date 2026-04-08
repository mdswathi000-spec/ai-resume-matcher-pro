import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

# This reads your HTML file and displays it
try:
    with open("AI_Resume_Matcher_Enhanced.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=1000, scrolling=True)
except FileNotFoundError:
    st.error("HTML file not found. Please ensure AI_Resume_Matcher_Enhanced.html is in the repository.")