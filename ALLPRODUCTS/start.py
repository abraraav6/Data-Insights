import streamlit as st
import pandas as pd
#Analytics Products
from analytical_products.anlyz import analyse_class
from analytical_products.exp import understand 
from analytical_products.viz import viz_class
# Train Test Products
from train_test_products.algo_cmp import algos
from train_test_products.clf_algo import clf_class
from train_test_products.regression import reg_class
#Predictable Products
from predictable_products.stocks import stock_prediction
from predictable_products.agri import agri_rec
from predictable_products.placement import placement_prediction
#Preprocessing Products
from preprocessing_products.prepare_data import clean_prepare_data
from preprocessing_products.miss_encode import prep_class
st.set_page_config(layout="wide")
data=pd.DataFrame()
analytics_opt=train_test_opt=predictio_opt=preprocessing_opt=" "
placeholder = st.empty()
class start_class:
    def fileupload(self):
            self.file=st.file_uploader('Upload file',type=['CSV','XLSX'])
            if self.file is not None:
                try:
                    self.data=pd.read_csv(self.file)
                    return self.data
                except:
                    try:
                        self.data=pd.read_excel(self.file)
                        return self.data
                    except:
                        st.warning('Supported CSV, EXCEL files only')
    def opt(self):
        self.option=st.sidebar.selectbox('Choose your Data Product',[" ","Analytical Products","Train and Test Products","Preprocessing Products","Predictable Products"])
        return self.option
if __name__=='__main__':
    session_state = st.session_state.setdefault('main_state', {})
    obj=start_class()
    data=obj.fileupload()
    opt=obj.opt()
    if data is not None:
            col1,col2,col3=st.columns(3)
            if opt=="Analytical Products":
                analytics_opt=st.selectbox("Choose your Analytical Product",["","Data Visualization","Data Analysis","Generate Report"])
                if analytics_opt=="Data Visualization":
                    if not session_state:
                        viz_class.viz_app(data)
                    else:
                        viz_class.viz_app(session_state.get("preprocessed_data"))
                if analytics_opt=="Data Analysis":
                    if not session_state:
                        analyse_class.analyse_fun(data)
                    else:
                        analyse_class.analyse_fun(session_state.get("preprocessed_data"))
                if analytics_opt=="Generate Report":
                    if not session_state:
                        understand.exp(data)
                    else:
                        understand.exp(session_state.get("preprocessed_data"))
            if opt=="Train and Test Products":
                train_test_opt=st.selectbox("Choose your Train and Test Product",["","Compare Algorithms","Regression","Classification"])
                if train_test_opt=="Compare Algorithms":
                    if not session_state:
                        algos.app(data)
                    else:
                        algos.app(session_state.get("preprocessed_data"))
                if train_test_opt=="Classification":
                    if not session_state:
                        clf_class.main(data)
                    else:
                        clf_class.main(session_state.get("preprocessed_data"))
                if train_test_opt=="Regression":
                    if not session_state:
                        reg_class.reg_app(data)
                    else:
                        reg_class.reg_app(session_state.get("preprocessed_data"))
            if opt=="Preprocessing Products":
                preprocessing_opt=st.selectbox("Choose your Preprocessing Product", options=[" ","Preprocessing","Missing values and Encode"])
                if preprocessing_opt=="Preprocessing":
                    preprocessed_data=clean_prepare_data.clean_prepare(data)
                    session_state['preprocessed_data'] = preprocessed_data
                if preprocessing_opt=="Missing values and Encode":
                    preprocessed_data= prep_class.preprocess(data)
                    session_state['preprocessed_data'] = preprocessed_data
    if opt=="Predictable Products":
        predictio_opt=st.selectbox("Choose your Predicatble Products",["","Stock market prediction","Agriculture Prediction","Placement Prediction"])
        if predictio_opt=="Stock market prediction":
            stock_prediction.stock_app()
        if predictio_opt=="Agriculture Prediction":
            data=pd.read_csv('agri_data.csv')
            agri_rec.agri_app(data)
        if predictio_opt=="Placement Prediction":
            data=pd.read_csv('collegePlace.csv')
            placement_prediction.plc_pred(data)
            