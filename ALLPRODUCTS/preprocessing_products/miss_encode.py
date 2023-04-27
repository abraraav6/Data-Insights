import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
class prep_class:
    def miss_values(data,cols):
        for i in cols:
            if data[i].dtype=="object":
                data[i]=data[i].fillna(data[i].mode().iloc[0])
            else:
                data[i]=data[i].fillna(data[i].mean())
    def convert(data,cols):
        # Initialize a LabelEncoder object
        label_encoder = LabelEncoder()
        # Loop through each column in the data
        for column in cols:
            # Check if the column contains categorical data
            if data[column].dtype == 'object':
                # Use the LabelEncoder object to transform the categorical data to numeric values
                data[column] = label_encoder.fit_transform(data[column])
    def norm(data):
        scaler = MinMaxScaler()
        data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    def preprocess(data):
        st.title("Start Preprocessing Missing values")
        st.warning("To enable encoding please fill missing values first")
        if data.isnull().sum().sum()>0:
            opt=st.selectbox("Automate or Manually deal with missing values", options=['','Automate','Manual filling'])
            st.write(data.isnull().sum())
            if opt=="Automate":
                prep_class.miss_values(data,data.columns)
                st.write(data.isnull().sum())
            if opt=="Manual filling":
                cols=[]
                for i in list(data.isnull().sum().index.values):
                    if data[i].isnull().sum()>0:
                        cols.append(i)
                cols=st.multiselect('Choose Columns',cols)
                prep_class.miss_values(data,cols)
                st.write(data.isnull().sum())
            if st.button('Reflect Data.'):
                preprocessed_data = data
                return preprocessed_data
        else:
            st.write('No missing data')
        if data.isnull().sum().sum()==0:
            st.title("Start encoding your Data")
            opt_enc=st.selectbox("Automate or Manually deal with categorical values", options=['','Automate','Manual filling'])
            l=list(data.select_dtypes(include=['object']).columns)
            st.write(data[l])
            if opt_enc=="Automate":
                prep_class.convert(data,data.columns)
                st.write(data[l])
            if opt_enc=="Manual filling":
                #cols = data.select_dtypes(include=['object']).columns
                col=st.multiselect("Choose columsn to Encode", options=data.columns)
                prep_class.convert(data,col)
                st.write(data[l])
            if st.button('Reflect Data'):
                preprocessed_data = data
                return preprocessed_data