import streamlit as st

about_text = '''
### Do you want to know more about me? 
### Schedule an apointment [here 🛸](https://api.whatsapp.com/send?phone=13439988190)
'''

st.set_page_config(
    page_title="Nicolas Peralta",
    page_icon="🧑🏻‍💻",
    initial_sidebar_state="expanded",
    menu_items={
        'About': about_text
    }
)

