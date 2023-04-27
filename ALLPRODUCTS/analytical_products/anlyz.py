import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
class analyse_class:
    def analyse_fun(data):
        try:
            st.title("Data Analysis App")
            col1,col2=st.columns(2)
            opt=st.selectbox("Select operation", options=["","Describe","Missing Information","Correlation","Value Count","Group By","View Data"])
            if opt=="View Data":
                st.write(data.head())
            if opt=='Describe':
                st.write(data.describe(include='all'))
            if opt=='Missing Information':
                st.write(data.isnull().sum())
            if opt=='Correlation':
                st.write(data.corr())
            if opt=="Value Count":
                c=st.selectbox("choose Value Counts Column",options=[" "]+list(data.columns))
                if c!=" ":
                    st.write(data.value_counts(c))
            if opt=="Group By":
                col=st.multiselect("Choose Column",data.columns)
                grp_col=st.multiselect("Choose col to opt",data.select_dtypes(exclude="object").columns)
                if len(col)!=0 and len(grp_col)!=0:
                    grouped=data.groupby(col)
                    st.write(grouped[grp_col].agg([np.mean,np.max,np.min,np.median,np.std]))
        except:
            st.warning("Choose Correct Columns")