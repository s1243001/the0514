import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
National Changhua University of Education
<https://www.ncue.edu.tw/>
"""

st.sidebar.title("About Our From")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("關於我們")
