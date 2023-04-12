import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pathlib import Path
import streamlit_authenticator as stauth
import os


st.set_page_config(page_title="Feedback Page", page_icon=":🌟:", layout="wide")

hide_st_style = """ <style> #MainMenu {visibility: hidden;} 
footer {visibility: hidden;} header {visibility: hidden;} 
</style> 
""" 
st.markdown(hide_st_style, unsafe_allow_html=True)


st.header(":mailbox: Get In Touch With Me!")
contact_form = """


<style>

/* Style inputs with type="text", type="email"and textareas */
input[type=text], input[type=email], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button[type=submit]:hover {
  background-color: #45a049;
}

pp.italic {
  font-style: italic;
}

</style>


<form action="https://formsubmit.co/poovarasankg@gmail.COM" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <p>Please select Prediction is Right or Wrong ?</p>
             <input type="radio" id="Right" name="pred_result" value="Right">
             <label for="Right">Right</label><br>
             <input type="radio" id="Wrong" name="pred_result" value="Wrong">
             <label for="Wrong">Wrong</label>
             <textarea name="message" placeholder="Any Suggestion Leave here..."></textarea>
             <button type="submit">Send</button>
            </form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
# Use Local CSS File style/style.css
#def local_css(file_name):
#    with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
 #        #<link rel='stylesheet' href='/css/style_file1.css'>
 #        local_css(r"multi_pred\pages\style")
