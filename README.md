# Machine Learning Web Application using Streamlit

This project demonstrates a simple binary classification web application built with [Streamlit](https://streamlit.io/). The goal is to predict whether mushrooms are [edible](https://en.wikipedia.org/wiki/Edible_mushroom) or [poisonous](https://en.wikipedia.org/wiki/Mushroom_poisoning) based on various features.

## Project Structure
- **app.py**: The main application script written in Python using the [Streamlit](https://streamlit.io/) library.
- **mushroom.csv**: The dataset containing information about mushroom, used for training and testing the machine learning models.

## Features
- **Binary Classification**: The app allows users to choose between different classifiers for binary classification:
  - Support Vector Machine (SVM)
  - Logistic Regression
  - Random Forest

- **Model Hyperparameters**: Users can customize model hyperparameters such as [regularization parameter](https://en.wikipedia.org/wiki/Regularization_(mathematics)), kernel type, and more.

- **Metrics Visualization**: The application provides visualizations for the following metrics:
  - [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
  - [ROC Curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
  - [Precision-Recall Curve](https://en.wikipedia.org/wiki/Precision_and_recall)

- **Show Raw Data**: Users have the option to display the raw mushroom dataset.

## Setup and Usage
1. **Clone the Repository**

	```bash
	git clone <https://github.com/SiddhiRohan/ml-webapp-streamlit.git>

2. **Install Dependencies:**
	
	```bash
	pip install -r requirements.txt

3. **Run the Streamlit App:**
	
	```bash
	streamlit run app.py

4. **Explore the Web App:**
Open your web browser and navigate to the provided Streamlit local development server URL.

## Usage Instructions

1. **Choose Classifier:**
- Use the sidebar to select the classifier of your choice: SVM, Logistic Regression or Random Forest.

2. **Set Model Hyperparameters:**
- Ajust model hyperparameters using the sliders and input fields in the sidebar.

3. **Classify:**
- Click the "Classify" button to train the selected model and view classification.

4. **Visualize Metrics:**
- Choose metrics to visualize (Confusion Matrix, ROC Curve, Precision-Recall Curve) using the sidebar.

5. **Show Raw Data:**
- Toggle the "Show raw data" checkbox to display the raw mushroom dataset.

## Dependencies
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
