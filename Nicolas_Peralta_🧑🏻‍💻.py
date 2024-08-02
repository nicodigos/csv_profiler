import streamlit as st
import pathlib
import sys

# This adds the path of the …/src folder
# to the PYTHONPATH variable
sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")


about_text = '''
### Do you want to know more about me? 
### Contact me [here 🛸](https://api.whatsapp.com/send?phone=13439988190)
'''

st.set_page_config(
    page_title="Nicolas Peralta",
    page_icon="🧑🏻‍💻",
    initial_sidebar_state="expanded",
    menu_items={
        'About': about_text
    }
)

