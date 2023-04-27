import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
class agri_rec:
    def agri_app(data):
        st.markdown("""<h2 style='color:green'>Crop Recommendation Engine</h2>""",unsafe_allow_html=True)
        #data=pd.read_csv('agri_data.csv')
        ls=list(data['label'].unique())
        rfc=RandomForestClassifier()
        le=LabelEncoder()
        data['label']=le.fit_transform(data['label'])
        ls_int=data['label']
        label_dict=dict(zip(ls,data['label'].unique()))
        xtr,xtes,ytr,ytes=train_test_split(data.iloc[:,:7],data.iloc[:,-1])
        fit=rfc.fit(xtr,ytr)
        st.title('Our Model Score')
        st.write(rfc.score(xtes,ytes))
        N=st.number_input('Enter Nitrogen Value')
        P=st.number_input('Enter Phosphorus Value')
        K=st.number_input('Enter Potassium Value')
        tem=st.number_input('Enter Temperature Value')
        hum=st.number_input('Enter Humidity Value')
        ph=st.number_input('Enter PH Value')
        rainfall=st.number_input('Enter RainFall Value')
        values=np.array([[N,P,K,tem,hum,ph,rainfall]])
        le=LabelEncoder()
        l=le.fit_transform(data['label'])
        if st.button('Predict'):
            result=le.inverse_transform(rfc.predict(values))
            st.markdown("""<h3 style='color:green'>From the data provided we recommed you</h1>""",unsafe_allow_html=True)
            st.title(result)
            st.write(label_dict)