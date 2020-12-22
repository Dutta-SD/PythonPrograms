# Coursera Guided Project for Building a web app using streamlit

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score

# Function for loading the data
@st.cache(persist = True)
    def load_data():
        '''Loads the csv file'''

        data = pd.read_csv('./mushrooms.csv')
        label = LabelEncoder()
        for col in data.columns:
            data[col] = label.fit_transform(data[col])
        return data

# Split the data into train and test dataframes
# Here we are using the mushroom dataset. So we drop 'type', which is target
@st.cache(persist = True)
    def split(df):
        '''Splits the dataframe into train and test'''

        y = df.type
        x = df.drop(['type'], axis = 1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
        return x_train, x_test, y_train, y_test


# which metrics to plot
def plot_metrics(metrics_list):
        '''Which metrics to plot'''

        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(model, x_test, y_test, display_labels= class_names)
            st.pyplot()
        
        if 'ROC Curve' in metrics_list:
            st.subheader('ROC Curve')
            plot_roc_curve(model, x_test, y_test)
            st.pyplot()

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader('PR- Curve')
            plot_precision_recall_curve(model, x_test, y_test)
            st.pyplot()

def svm_Model_Launch():
    ''' Starts SVM Model for the Web App'''
    # Support Vector Machines
        st.sidebar.subheader("Model Hyperparameters")

        # C-regularisation parameter
        C = st.sidebar.number_input("C (Regularisation)",
        0.01, 
        10.0, 
        step = 0.01, 
        key = 'C')

        # kernel for SVM
        kernel = st.sidebar.radio("kernel", ("rbf", "linear"), key = 'kernel')

        # Gamma parameter for SVM
        gamma = st.sidebar.radio("Gamma", ("scale", "auto"), key = 'gamma')

        # Selection for sidebar
        metrics = st.sidebar.multiselect('What metrics do you want?', ('Confusion Matrix',
        'ROC Curve', 'Precision-Recall Curve'))

        
        if st.sidebar.button("Classify", key = 'classify'):
            st.subheader("Support Vector Machine")
            model = SVC(C = C, kernel = kernel, gamma = gamma)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_preds = model.predict(x_test)

            st.write("Accuracy = ", accuracy.round(2))
            st.write("precision ", precision_score(y_test, y_preds, labels = class_names).round(2))
            st.write("recall ", recall_score(y_test, y_preds, labels = class_names).round(2))
            plot_metrics(metrics)

def logistic_Regression_model_launch():
    st.sidebar.subheader("Model Hyperparameters")
        C = st.sidebar.number_input("C (Regularisation)",
        0.01, 10.0, step = 0.01, key = 'C_LR')
        max_iter = st.sidebar.slider("Max number of iterations", 100, 500, key = 'max_iter')


        metrics = st.sidebar.multiselect('What metrics do you want?', ('Confusion Matrix',
        'ROC Curve', 'Precision-Recall Curve'))

        if st.sidebar.button("Classify", key = 'classify'):
            st.subheader("Logistic Regression")
            model = LogisticRegression(C = C, max_iter=max_iter)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_preds = model.predict(x_test)

            st.write("Accuracy = ", accuracy.round(2))
            st.write("precision ", precision_score(y_test, y_preds, labels = class_names).round(2))
            st.write("recall ", recall_score(y_test, y_preds, labels = class_names).round(2))
            plot_metrics(metrics)

def random_Forest_model_launch():
    st.sidebar.subheader("Model Hyperparameters")
        n_estimators = st.sidebar.number_input("Number of Estimators", 100, 5000, step = 10, 
        key = "n_estimators")

        max_depth = st.sidebar.number_input('Max Depth of the tree', 1, 20, step =1, key = 'max_depth' )
        bootstrap = st.sidebar.radio("Bootstrap? ", ('True', 'False'), key = 'bootstrap')
        metrics = st.sidebar.multiselect('What metrics do you want?', ('Confusion Matrix',
        'ROC Curve', 'Precision-Recall Curve'))

        if st.sidebar.button("Classify", key = 'classify'):
            st.subheader("Random Forest Regression")
            model = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators,
            bootstrap=bootstrap)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_preds = model.predict(x_test)

            st.write("Accuracy = ", accuracy.round(2))
            st.write("precision ", precision_score(y_test, y_preds, labels = class_names).round(2))
            st.write("recall ", recall_score(y_test, y_preds, labels = class_names).round(2))
            plot_metrics(metrics)


def main():
    ''' Launches the web app'''

    # Title of the Web App
    st.title('Binary Classification Web App')

    # SideBar title
    st.sidebar.title('Binary Classification Web App')

    # Add MarkDown text in Main body of web app
    st.markdown('Are you mushrooms **edible** or **not**')
    
    df = load_data() # Get the data

    x_train, x_test, y_train, y_test = split(df)  ## Split it

    # Stores the class names, edible or poisonous mushroom
    class_names = ['Edible', 'Poisonous']

    # Add Subheader
    st.sidebar.subheader("Choose Classifiers")

    # drop down menu of sidebar
    classifier = st.sidebar.selectbox("Classifier",
    ('SVC', 'Logistic Regression', 'Random Forest'))
    
    # Functionality for each method
    if classifier == 'SVC':
        svm_Model_Launch()

    if classifier == 'Logistic Regression':
        logistic_Regression_model_launch()
    # Random Forest
    if classifier == 'Random Forest':
        random_Forest_model_launch()        

    # Actual options tuple o string
    if st.sidebar.checkbox("Show raw data", False):
        st.subheader("Mushroom Data Set")
        st.write(df)

if __name__ == '__main__':
    main()