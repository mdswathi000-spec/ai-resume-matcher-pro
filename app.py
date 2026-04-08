import streamlit as st
import streamlit.components.v1 as components

# Forces wide mode and hides the sidebar
st.set_page_config(page_title="Resume Matcher Pro", layout="wide", initial_sidebar_state="collapsed")

# Professional CSS to remove all Streamlit borders and padding
st.markdown("""
    <style>
        /* Hide Streamlit elements */
        header, footer, #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Force the container to fill 100% of the screen width and height */
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            width: 100% !important;
            height: 100vh !important;
            border: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

try:
    with open("AI_Resume_Matcher_Enhanced.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Render the HTML at full width
    components.html(html_code, height=2000, scrolling=True)
except FileNotFoundError:
    st.error("HTML file not found in repository.")