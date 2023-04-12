import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

hide_st_style = """ <style> #MainMenu {visibility: hidden;} 
footer {visibility: hidden;} header {visibility: hidden;} 
</style> 
""" 
st.markdown(hide_st_style, unsafe_allow_html=True)

st.set_page_config(page_title="Graphical View", page_icon=":♨:", layout="wide")

hide_st_style = """ <style> #MainMenu {visibility: hidden;} 
footer {visibility: hidden;} header {visibility: hidden;} 
</style> 
""" 
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header("Multi Graphical View")

html_temp = """
<div style ="background-color:burlywood;padding:13px">
<h5 style ="color:black;text-align:center;">In the below pie chart, the ratio of different classifier algorithms is represented.
Here, the   K-Nearest Neighbour (KNN) algorithm gets the maximum amount of accuracy.
As a result, in this ML model trained by the KNN classifier.</h5>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)

#st.write('''In the below pie chart, the ratio of different classifier algorithms is represented.
#Here, the K-Nearest Neighbour (KNN) algorithm gets the maximum amount of accuracy. \n
#As a result, in this ML model trained by the KNN classifier''')

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'SVM', 'RF', 'NB', 'LOR', 'LIR', 'KNN', 'GB RE', 'GB CL', 'DT'
sizes = [74, 82, 82, 78, 50, 86, 64, 85, 85]
explode = (0, 0, 0, 0, 0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


html_temp = """
<div style ="background-color:burlywood;padding:13px">
<h5 style ="color:black;text-align:center;">In the below comparison chart, represent the total number of datasets and show the difference between the number of placed and non-placed students, respectively.</h5>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)


#st.write('''In the below comparison chart, represent the total number of datasets and show the difference between the number of placed and non-placed students, respectively.''')


# 2966 continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
df = pd.DataFrame(
    [["Placed Student Count", 1639], [" Non Placed Student Count", 1327]],
    columns=["Bar Chart", "Out of 2966 Students"]
)

fig = px.bar(df, x="Bar Chart", y=["Out of 2966 Students"], barmode='group', height=600)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)
