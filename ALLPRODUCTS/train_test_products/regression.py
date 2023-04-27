import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import streamlit as st
class reg_class:
    def reg_app(data):
        st.title("Regression Model Builder")
        
        # Upload the CSV file
        try:
                x_columns = st.multiselect("Choose the x columns", data.columns)
                y_column = st.selectbox("Choose the y column", data.columns)
        
                # Check for missing and categorical values in the selected x columns
                selected_data = data[x_columns + [y_column]]
                missing_values = selected_data.isnull().values.any()
                categorical_values = selected_data.select_dtypes(include=['object', 'category']).columns
        
                if missing_values or len(categorical_values) > 0:
                    st.warning("The selected x columns contain missing or categorical values. Please select different x columns or preprocess the data before training the model.")
                else:
                    # Choose the regression model
                    model_name = st.selectbox("Choose a regression model", ["Linear Regression", "Lasso Regression", "Ridge Regression", "Elastic Net Regression", "K-Neighbors Regression", "Decision Tree Regression", "Random Forest Regression"])
        
                    # Train the regression model
                    x = data[x_columns].values
                    y = data[y_column].values
        
                    if model_name == "Linear Regression":
                        model = LinearRegression()
                    elif model_name == "Lasso Regression":
                        model = Lasso()
                    elif model_name == "Ridge Regression":
                        model = Ridge()
                    elif model_name == "Elastic Net Regression":
                        model = ElasticNet()
                    elif model_name == "K-Neighbors Regression":
                        n_neighbors = st.slider("Choose the number of neighbors", min_value=1, max_value=100, value=5)
                        model = KNeighborsRegressor(n_neighbors=n_neighbors)
                    elif model_name == "Decision Tree Regression":
                        max_depth = st.slider("Choose the maximum depth", min_value=1, max_value=100, value=5)
                        model = DecisionTreeRegressor(max_depth=max_depth)
                    elif model_name == "Random Forest Regression":
                        n_estimators = st.slider("Choose the number of trees", min_value=1, max_value=100, value=10)
                        max_depth = st.slider("Choose the maximum depth", min_value=1, max_value=100, value=5)
                        model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
        
                    model.fit(x, y)
        
                    # Make predictions
                    if x_columns and y_column and model_name:
                        selected_data = data[x_columns + [y_column]]
                        missing_values = selected_data.isnull().values.any()
                        categorical_values = selected_data.select_dtypes(include=['object', 'category']).columns
            
                        if missing_values or len(categorical_values) > 0:
                            st.warning("The selected x columns contain missing or categorical values. Please select different x columns or preprocess the data before making predictions.")
                        else:
                            x_input = []
                            for column in x_columns:
                                value = st.number_input(f"Enter a value for the {column} column")
                                x_input.append(value)
            
                            x_input = np.array(x_input).reshape(1, -1)
                            y_pred = model.predict(x_input)[0]
                            if st.button("Predict"):
                                st.write(f"The predicted value for {y_column} is {y_pred:.2f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
