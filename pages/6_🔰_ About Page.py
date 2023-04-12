import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pathlib import Path
import streamlit_authenticator as stauth

st.set_page_config(page_title="About Page", page_icon=":🔰:", layout="wide")


st.header(":gear: About Me!")
st.write('''MSPP - Multi Student Placement Prediction System v1.0. - 
Its an STREAMLIT based web Application. \n
developed by, \n
Poovarasan K  \n
Passionate 🖥 Software Developer 🖥\n
Contact me at  📬 poovarasankg@gmail.com 📫
''')
#st.markdown(html_temp, unsafe_allow_html = True)
#authenticator.logout("Logout")
#st.header(f"Welcome {name}")
