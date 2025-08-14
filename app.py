import streamlit as st

# Read your HTML file
with open("main.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display in Streamlit
st.components.v1.html(html_code, height=700, scrolling=True)
