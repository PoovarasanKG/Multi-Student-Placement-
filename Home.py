import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pathlib import Path
import streamlit_authenticator as stauth

st.set_page_config(page_title="Placement Prediction Dashboard", page_icon=":bar_chart:", layout="wide")

hide_st_style = """ <style> #MainMenu {visibility: hidden;} 
footer {visibility: hidden;} header {visibility: hidden;} 
</style> 
""" 
st.markdown(hide_st_style, unsafe_allow_html=True)



hide_bar= """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        visibility:hidden;
        width: 0px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        visibility:hidden;
    }
    </style>
"""
st.title("SPARKA - Multi Student Placement Prediction System")
title_alignment=""" <style> 
#the-title {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

#--- USER AUTHNTICATION --- 

names = ["Student"]
usernames = ["admin"]
# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "SIPL_dashboard", "abcdef")
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status == None:
    st.warning("username - admin, Password - 123 ")
    st.warning("Please enter your username and password")
    st.markdown(hide_bar, unsafe_allow_html=True)
#selected = option_menu(menu_title="mmain", options=['Home', 'Academic Details Prediction', 'Skillset Information Prediction', 'FeedBack', 'About'], icons=['house','activity','kanban','heart','app-indicator'], default_index=0)
if authentication_status:
    st.header(f"Welcome {name}")
    st.write('''This is an online streaming web application. It is used to forecast student placement possibilities. based on their native information. \n
              Use the navigation 👈 sidebar to move the multi directional functions. \n Happy 😊 Predictio.''')
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write("   ")
    authenticator.logout("Logout")
