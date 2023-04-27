import streamlit as st
import pandas as pd
class clean_prepare_data:
    def clean_prepare(data):
            st.title('Data Cleaning and Preparation')
            st.write(data)
            st.header('Data with basic stats')
            st.write(data.describe())
            st.header('Missing values count in each column')
            st.write(data.isnull().sum())
            st.warning('If columns with more than 50% missing please do remove it or gather data again')
            if data.isnull().sum().sum()>0:
                st.title('Recommended to fill missing values')
                miss_con=st.radio('Conform to continue',['','Yes','No'])
                if miss_con=='Yes':
                    st.header('Numerical Columns with missing values')
                    num_col=data.select_dtypes(include=['int64','float64'])
                    st.write(num_col)
                    st.header('Categorical Columns with missing values')
                    cat_col=data.select_dtypes(exclude=['int64','float64'])
                    st.write(cat_col)
                    st.header('Fill Numerical Columns with missing values with Mean or Median')
                    miss_num_opt=st.radio('Choose to continue',['','Mean','Median'])
                    l_num=list(num_col.columns)
                    if miss_num_opt=='Mean':
                        for i in l_num:
                            data[i].fillna(data[i].mean(),inplace=True)
                        st.header('Missing values count in each column')
                        st.write(data.isnull().sum())
                    elif miss_num_opt=='Median':
                        for i in l_num:
                            data[i].fillna(data[i].median(),inplace=True)
                        st.header('Missing values count in each column')
                        st.write(data.isnull().sum())
                    st.header('Fill Categorical Columns with missing values with Mode or Forward Fill or Backward Fill')
                    miss_cat_opt=st.radio('Choose to continue',['','Mode','Forward_Fill','Backward_Fill'])
                    l_cat=list(cat_col.columns)
                    if miss_cat_opt=='Mode':
                        for i in l_cat:
                            data[i].fillna(data[i].mode(),inplace=True)
                        st.header('Missing values count in each column')
                        st.write(data.isnull().sum())
                    elif miss_cat_opt=='Forward_Fill':
                        for i in l_cat:
                            data[i].fillna(method='ffill',inplace=True)
                        st.header('Missing values count in each column')
                        st.write(data.isnull().sum())
                    elif miss_cat_opt=='Backward_Fill':
                        for i in l_cat:
                            data[i].fillna(method='bfill',inplace=True)
                        st.header('Missing values count in each column')
                        st.write(data.isnull().sum())
                    elif miss_con=='No':
                        st.warning('Please do fill it for further analysis, if not you may end up with wrong decision')
                    if st.button('Reflect Data'):
                        preprocessed_data = data
                        return preprocessed_data
            else:
                st.write('Good to go for further Analysis')
                st.balloons()