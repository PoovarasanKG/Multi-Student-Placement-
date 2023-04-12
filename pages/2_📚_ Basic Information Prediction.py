import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pathlib import Path
import streamlit_authenticator as stauth

import os

import joblib
from io import BytesIO

import requests # or https

st.set_page_config(page_title="Basic Info Prediction", page_icon=":📚:", layout="wide")


# loading the saved models
#basic_model = pickle.load(open('model.pkl', 'rb'))
#basic_model = pickle.load(open('multi_pred/pages/model.pkl','rb'))

#location = r'C:\Users\poova\Desktop\multi_pred\pages'
#fullpath = os.path.join(location,'model.pkl')
#basic_model = pickle.load(open(fullpath,'rb'))  


URI = "https://github.com/PoovarasanKG/Multi-Student-Placement-/blob/main/pages/model.pkl"
basic_model = pickle.load(open('URI', 'rb'))
#joblib.load(BytesIO(requests.get(URI).content))


st.title('Student Placement Prediction Application')

html_temp ="""
<div style ="background-color:yellow;padding:13px">
<h1 style ="color:black;text-align:center;">Basic Information Prediction using ML - KNN Classifier </h1>
</div>
"""
                    
                # this line allows us to display the front end aspects we have
                # defined in the above code
st.markdown(html_temp, unsafe_allow_html = True)
gender = st.number_input("Enter Gender( Female 👉 0, Male 👉 1)", step=1, value=0)
stream = st.number_input("Enter Stream( Civil 👉 0  ,CSE 👉 1, Electronics 👉 2, EnTC 👉 3, IT 👉 4, Mechanical 👉 5)",step=1, value=0)
intern = st.number_input("Enter Previous Internships",step=1, value=0)
cgpa = st.number_input("Enter CGPA",step=1, value=0)
backlogs = st.number_input("Enter backlogs",step=1, value=0)	
# code for Prediction
result_baisc =""
# creating a button for Prediction
if st.button('Predict The Result'):
        basic_pred = basic_model.predict([[gender, stream, intern, cgpa, backlogs]])
        if (basic_pred[0] == 1):
            result_baisc = "You have the opportunity to join a company."
            st.success(result_baisc)
            st.success("Good luck, and your studies will continue to prepare you for your future career...")
        else:
            result_baisc = "You don't have the opportunity to join."
            st.success(result_baisc)
            st.success("Better luck next time, and your studies will focus on your CGPA and clearing your backlogs for future career advancement...")
            #st.success(result_baisc)
