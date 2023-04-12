import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pathlib import Path
import streamlit_authenticator as stauth
import os

from io import BytesIO
import io
from bytesbufio import BytesBufferIO
import requests # or https

hide_st_style = """ <style> #MainMenu {visibility: hidden;} 
footer {visibility: hidden;} header {visibility: hidden;} 
</style> 
""" 
st.markdown(hide_st_style, unsafe_allow_html=True)

mLink = 'https://github.com/PoovarasanKG/Multi-Student-Placement-/blob/main/pages/model_place.pkl?raw=true'
mfile = BytesBufferIO(requests.get(mLink).content)
place_model = pickle.load(mfile)


st.set_page_config(page_title="Placement Info Prediction", page_icon=":📄:", layout="wide")


# loading the saved models
#place_model = pickle.load(open('model_place.pkl', 'rb'))

#location = r'C:\Users\poova\Desktop\multi_pred\pages'
#fullpath = os.path.join(location,'model_place.pkl')
#place_model = pickle.load(open(fullpath,'rb'))

st.title('Student Placement Prediction Application')
html_temp = """
<div style ="background-color:yellow;padding:13px">
<h1 style ="color:black;text-align:center;">Placement Skillset Information Prediction using ML - KNN Classifier</h1>
</div>
"""
# this line allows us to display the front end aspects we have
# defined in the above code
st.markdown(html_temp, unsafe_allow_html = True)

quants = st.number_input("Enter Quants(Please Enter 1 to 25 of Score)", step=1, value=0)
logical = st.number_input("Enter LogicalReasoning (Please Enter 1 to 25 of Score)",step=1, value=0)
verbal = st.number_input("Enter Verbal (Pleace Enter 1 to 25 of Score)",step=1, value=0)
program = st.number_input("Enter Programming (Please Enter 1 to 25 of Score)",step=1, value=0)
cgpa = st.number_input("Enter CGPA (Please Enter 1 to 10 of Grade)",step=1, value=0)	
# code for Prediction
result_place =""     
# creating a button for Prediction
if st.button('Predict The Result'):
    place_pred = place_model.predict([[quants, logical, verbal, program, cgpa]])                          
    if (place_pred[0] == 1):
        result_place = "You have the opportunity to join a company"
        st.success(result_place)
        st.success("Congratulations on being placed Keep in touch with your abilities and progress. Learn new technologies...")
    else:
        result_place = "You don't have the opportunity to join."
        st.success(result_place)
        st.success("Sorry for conveying this, please concentrate on your programming skills and aptidudes!")
