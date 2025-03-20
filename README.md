# Thyroid Disorder Prediction

This project aims to predict thyroid disorders, particularly hypothyroidism, using machine learning models. The project includes data preprocessing, logistic regression modeling, and a Streamlit-based web application for interactive analysis and visualization.

## Project Overview

Thyroid disorders, especially hypothyroidism, are common conditions where the thyroid gland is underactive, leading to various health issues. This project uses a dataset containing patient information and laboratory results to predict the likelihood of thyroid disorders.

## Key Features

- **Logistic Regression Model**: A logistic regression model is used to predict the likelihood of hypothyroidism based on various features.
- **ROC Curve & AUC Score**: The model's performance is evaluated using the ROC curve and the AUC score.
- **Feature Importance**: The importance of different features in predicting thyroid disorders is determined.
- **Visualization**: Various visualizations, including ROC curves and feature importance charts, are included for better understanding of the model and results.

## Project Structure

The project is organized into the following sections:

1. **Data Preprocessing**: Cleaning and transforming the dataset into a suitable format for training the machine learning model.
2. **Model Training**: Training a logistic regression model using the preprocessed data.
3. **Model Evaluation**: Evaluating the performance of the trained model using metrics like ROC curve, AUC score, and accuracy.
4. **Visualization**: Visualizing the model's performance and important features using charts and plots.

## Requirements

To run this project, you'll need to install the following dependencies:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `streamlit`
