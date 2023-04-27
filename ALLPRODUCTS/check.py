import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
def main():
    st.title("Classification Model Training and Prediction")
    st.write("Upload a CSV file and select the X and Y columns for classification model training.")
    file = st.file_uploader("Upload CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write(df.head())
        
        x_columns = st.multiselect("Select X columns", df.columns.tolist())
        y_column = st.selectbox("Select Y column", df.columns.tolist())
        
        if x_columns and y_column:
            if set(df[y_column].unique()) == {0, 1}:
                st.write("Binary classification problem")
                preprocess = False
            else:
                st.write("Multi-class classification problem")
                preprocess = True
                # Add code for preprocessing categorical columns
            train_model(df[x_columns], df[y_column], preprocess)
def train_model(X, y, preprocess):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    models = {"Logistic Regression": LogisticRegression(),
              "Naive Bayes": GaussianNB(),
              "Decision Tree": DecisionTreeClassifier(),
              "Random Forest": RandomForestClassifier()}
    
    if preprocess:
        categorical_columns = X.select_dtypes(include=["object"]).columns.tolist()
        if categorical_columns:
            X_train = pd.get_dummies(X_train, columns=categorical_columns)
            X_test = pd.get_dummies(X_test, columns=categorical_columns)

    for name, model in models.items():
        st.write(f"Training {name} model...")
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        st.write(f"{name} model accuracy: {accuracy}")

        if st.button(f"Make {name} model predictions"):
            new_data = {} # create empty dictionary to store user input for new data
            for column in X.columns.tolist():
                new_data[column] = st.text_input(f"Enter {column}")
            if preprocess and categorical_columns:
                new_data_df = pd.DataFrame(new_data, index=[0])
                new_data_df = pd.get_dummies(new_data_df, columns=categorical_columns)
                new_data = new_data_df.to_dict(orient="records")[0]
            prediction = model.predict(pd.DataFrame(new_data, index=[0]))
            st.write(f"{name} model prediction: {prediction}")

    # Allow user to make predictions on new data
    st.write("\n\nEnter values for new data:")
    new_data = {}
    for column in X.columns.tolist():
        new_data[column] = st.text_input(f"Enter {column}")

    if preprocess and categorical_columns:
        new_data_df = pd.DataFrame(new_data, index=[0])
        new_data_df = pd.get_dummies(new_data_df, columns=categorical_columns)
        new_data = new_data_df.to_dict(orient="records")[0]

    if st.button("Make predictions on new data"):
        for name, model in models.items():
            prediction = model.predict(pd.DataFrame(new_data, index=[0]))
            st.write(f"{name} model prediction: {prediction}")

if __name__=="__main__":
    main()