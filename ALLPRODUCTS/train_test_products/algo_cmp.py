import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from sklearn.model_selection import train_test_split
#Regression 
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, max_error, mean_absolute_error, median_absolute_error
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
# classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
class algos:
    def app(df):
            st.title("Algorithm Comparison")
            st.write(df)
            st.title("Model Training App")
            option = st.selectbox('Choose types of models?',(' ', 'Classification', 'Regression'))
            if option=='Regression':
                    x_col = st.multiselect("Select X Column", df.columns)
                    y_col = st.selectbox("Select Y Column", df.columns)
                    if st.button('Predict'):
                        X = df[x_col]
                        y = df[y_col]
                        try:
                            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                            models = {
                "Linear Regression": LinearRegression(),
                "Ridge Regression": Ridge(),
                "Lasso Regression": Lasso(),
                "ElasticNet Regression": ElasticNet(),
                "Decision Tree Regressor": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "Gradient Boosting Regressor": GradientBoostingRegressor()
            }
                            metrics={}
                            for name, model in models.items():
                                # Train the model
                                model.fit(X_train, y_train)
                                
                                # Make predictions on the test data
                                y_pred = model.predict(X_test)
                        
                                # Compute the mean squared error of the model
                                mse = mean_squared_error(y_test, y_pred)
                                r2 = r2_score(y_test, y_pred)
                                evs = explained_variance_score(y_test, y_pred)
                                me = max_error(y_test, y_pred)
                                mae = mean_absolute_error(y_test, y_pred)
                                medae = median_absolute_error(y_test, y_pred)
                                # Display the mean squared error of the model
                                st.title(name)
                                st.write("Mean Squared Error:", mse)
                                st.write("Mean Squared Error:", mse)
                                st.write("R-squared Score:", r2)
                                st.write("Explained Variance Score:", evs)
                                st.write("Max Error:", me)
                                st.write("Mean Absolute Error:", mae)
                                st.write("Median Absolute Error:", medae)
                                metrics[name] = {
                    "Mean Squared Error": mse,
                    "R-squared Score": r2,
                    "Explained Variance Score": evs,
                    "Max Error": me,
                    "Mean Absolute Error": mae,
                    "Median Absolute Error": medae
                }
                            metric_names = list(metrics["Linear Regression"].keys())
                            model_names = list(models.keys())
                            metric_values = [[metrics[model_name][metric_name] for metric_name in metric_names] for model_name in model_names]
                            df_metrics = pd.DataFrame.from_dict(metrics).melt(ignore_index=False, var_name='Model', value_name='Metric Value')
                            df_metrics['Metric'] = df_metrics.index.get_level_values(0)
    
                            fig = px.bar(df_metrics, x='Model', y='Metric Value', color='Metric', barmode='group')
                
                            fig.update_layout(
                xaxis_title="Model",
                yaxis_title="Metric Value",
                height=600,
                width=1000,
            )
                            st.title("Comparison of Regression Models")
    
                            st.write(fig)
    
    
                        except:
                            st.warning('The data you have is not preprocessed')
            if option=='Classification':
                x_col = st.selectbox("Select X Column", df.columns)
                y_col = st.selectbox("Select Y Column", df.columns)
                if st.button('Predict'):
                    # Create X and y arrays
                    X = df[[x_col]]
                    y = df[y_col]
                    clf_names = []
                    acc_scores = []
                    prec_scores = []
                    rec_scores = []
                    f1_scores = []
                    try:
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                        clf_lr = LogisticRegression()
                        clf_knn = KNeighborsClassifier(n_neighbors=5)
                        clf_dt = DecisionTreeClassifier(max_depth=5)
                        clf_rf = RandomForestClassifier(n_estimators=10)
                        clf_svc = SVC(kernel='linear')
                        classifiers = [('Logistic Regression', clf_lr), ('K-Nearest Neighbors', clf_knn), ('Decision Tree', clf_dt), ('Random Forest', clf_rf), ('Support Vector Machines', clf_svc)]
                        for clf_name, clf in classifiers:
                            clf.fit(X_train, y_train)
                            y_pred = clf.predict(X_test)
                            acc = accuracy_score(y_test, y_pred)
                            prec = precision_score(y_test, y_pred, average='weighted')
                            rec = recall_score(y_test, y_pred, average='weighted')
                            f1 = f1_score(y_test, y_pred, average='weighted')
                            clf_names.append(clf_name)
                            acc_scores.append(acc)
                            prec_scores.append(prec)
                            rec_scores.append(rec)
                            f1_scores.append(f1)
                        data = pd.DataFrame({
                            'Classifier': clf_names,
                            'Accuracy': acc_scores,
                            'Precision': prec_scores,
                            'Recall': rec_scores,
                            'F1 Score': f1_scores
                        })
    
                        # Melt dataframe for easier plotting
                        melted = pd.melt(data, id_vars=['Classifier'], var_name='Metric', value_name='Score')
    
                        # Create bar chart using Plotly Express
                        fig = px.bar(melted, x='Classifier', y='Score', color='Metric', barmode='group')
                        st.write(fig)
                    except:
                        st.write('sorry')