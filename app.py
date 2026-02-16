import streamlit as st
from PIL import Image

# Hide the sidebar and the default Streamlit menu
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Hide the header and menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load the image
image = Image.open("image.png")

# Display the image full screen
st.image(image, use_column_width=True)
