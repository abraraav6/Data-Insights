import pandas as pd
import streamlit as st
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
class placement_prediction:
    def plc_pred(data):
        st.markdown("""<h2 style='color:green'>Placement Prediction</h2>""",unsafe_allow_html=True)
        #data=pd.read_csv('collegePlace.csv')
        rfc=RandomForestClassifier()
        le=LabelEncoder()
        data['Stream']=le.fit_transform(data['Stream'])
        data['Gender']=le.fit_transform(data['Gender'])
        fit=rfc.fit(data[['Age','Gender','Stream','Internships','CGPA','HistoryOfBacklogs']],data['PlacedOrNot'])
        age=st.number_input('Enter your age')
        gender=st.selectbox('Select Gender', options=["Male","Female"])
        stream=st.selectbox("Select Stream", options=["Computer Science","Information Technology","Electronics And Communication","Mechanical","Electrical","Civil"])
        stream_int=["Civil","Computer Science","Electronics And Communication","Information Technology","Mechanical"]
        if stream in stream_int:
            stream=stream_int.index(stream)
        if gender=="Male":
            gender=1
        if gender=="Female":
            gender=0
        internship=st.number_input("Number of Internships")
        cgpa=st.number_input("Enter your CGPA")
        backlogs=st.number_input("Number of Backlogs")
        values=np.array([[age,gender,stream,internship,cgpa,backlogs]])
        if st.button("Predict"):
            result=rfc.predict(values)
            if result==1:
                st.title("Congratulations you will be placed")
                st.balloons()
            if result==0:
                if int(internship)==0:
                    st.warning("Try doing Internships")
                if int(backlogs)>=1:
                    st.warning("Try clearing the Backlogs")
                if cgpa<6.0:
                    st.warning("Study Concepts correctly")