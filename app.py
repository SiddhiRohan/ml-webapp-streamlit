import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, auc, plot_roc_curve, precision_recall_curve
from sklearn.metrics import precision_score, recall_score 


def main():
    st.title("Binary Classification Web App")
    st.sidebar.title("Binary Classification Web App")
    st.markdown("Are your mushrooms edible or poisonous? 🍄")
    st.sidebar.markdown("Are your mushrooms edible or poisonous? 🍄")

    @st.cache(persist=True)
    def load_data():
        data = pd.read_csv("mushrooms.csv")

        df_copy = data.copy()

        label = LabelEncoder()

        df_copy['type'] = label.fit_transform(df_copy['type'])

        for col in df_copy.columns:
            df_copy[col] = label.fit_transform(df_copy[col])

        return df_copy

    @st.cache(persist=True)
    def split(df):
        y = df['type'].values
        x = df.drop(columns=['type']).values
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        return x_train, x_test, y_train, y_test

    def plot_metrics(metrics_list):
        fig, ax = plt.subplots()
        
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(model, x_test, y_test, display_labels=class_names, ax=ax)
            st.pyplot(fig)
        
        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            fig, ax = plt.subplots()
            plot_roc_curve(model, x_test, y_test, ax=ax)
            st.pyplot(fig)

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader("Precision-Recall Curve")
            y_probs = model.predict_proba(x_test)[:, 1]
            precision, recall, _ = precision_recall_curve(y_test,y_probs)
            fig, ax = plt.subplots()
            ax.step(recall, precision, where='post')
            ax.set_xlabel('Recall')
            ax.set_ylabel('Precision')
            ax.set_title('Precision-Recall Curve')
            st.pyplot(fig)

    df = load_data()
    x_train, x_test, y_train, y_test = split(df)
    class_names = ['edible', 'poisonous']
    st.sidebar.subheader("Choose classififer")
    classifier = st.sidebar.selectbox("Classifier", ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

    if classifier == 'Support Vector Machine (SVM)':
        st.sidebar.subheader("Model Hyperparameters")
        C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C')
        kernel = st.sidebar.radio("Kernel", ("rbf", "linear"), key='kernel')
        gamma = st.sidebar.radio("Gamma (Kernel Coefficient",("scale", "auto"), key ='gamma')

        metrics = st.sidebar.multiselect("What metrics to plot?",('Confusion Matrix', 'ROC Curve','Precision-Recall Curve'))

        if st.sidebar.button("Classify", key='classify'):
            st.subheader("Support Vector Machine (SVM) Results")
            model = SVC(C=C, kernel=kernel, gamma=gamma, probability=True)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_pred = model.predict(x_test)
            st.write("Accuracy: ", accuracy)
            st.write("Precision: ", precision_score(y_test, y_pred, labels=class_names))
            st.write("Recall: ", recall_score(y_test, y_pred, labels=class_names))
            plot_metrics(metrics)
    
    if classifier == 'Logistic Regression':
        st.sidebar.subheader("Model Hyperparameters")
        C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_LR')
        max_iter = st.sidebar.slider("Maximum number of iterations", 100, 500, key='max_iter')

        metrics = st.sidebar.multiselect("What metrics to plot?",('Confusion Matrix', 'ROC Curve','Precision-Recall Curve'))

        if st.sidebar.button("Classify", key='classify'):
            st.subheader("Logistic Regression Results")
            model = LogisticRegression(C=C, max_iter=max_iter)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_pred = model.predict(x_test)
            st.write("Accuracy: ", accuracy)
            st.write("Precision: ", precision_score(y_test, y_pred, labels=class_names))
            st.write("Recall: ", recall_score(y_test, y_pred, labels=class_names))
            plot_metrics(metrics)

    if classifier == 'Random Forest':
        st.sidebar.subheader("Model Hyperparameters")
        n_estimators = st.sidebar.number_input("The number of trees in the forest", 100, 5000, step=10, key='n_estimators')
        max_depth = st.sidebar.number_input("The maximum depth of the tree", 1, 20, step=1, key='max_depth')
        metrics = st.sidebar.multiselect("What metrics to plot?",('Confusion Matrix', 'ROC Curve','Precision-Recall Curve'))
        bootstrap = st.sidebar.checkbox("Bootstrap samples when building trees", value=True, key='bootstrap')

        if st.sidebar.button("Classify", key='classify'):
            st.subheader("Random Forest Results")
            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, bootstrap=bootstrap, n_jobs=-1)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_pred = model.predict(x_test)
            st.write("Accuracy: ", accuracy)
            st.write("Precision: ", precision_score(y_test, y_pred, labels=class_names))
            st.write("Recall: ", recall_score(y_test, y_pred, labels=class_names))
            plot_metrics(metrics)
        



    if st.sidebar.checkbox("Show raw data", False):
        st.subheader("Mushroom Data Set for (Classification)")
        st.write(df)



if __name__ == '__main__':
    main()
