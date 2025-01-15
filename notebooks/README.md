# Task 1: Exploration of Customer Purchasing Behavior

Exploratory Data Analysis (EDA) is a crucial step in every meaningful machine learning project. It helps uncover the nature of the data, informs the modeling approach, and reveals potential insights about the problem domain. This task focuses on exploring customer purchasing behavior in Rossmann Pharmaceuticals' stores.

## Objective
The goal of this task is to:
- Analyze customer behavior in various stores.
- Understand the impact of promotions and the opening of new stores on purchasing patterns.
- Prepare the data for further analysis and modeling by addressing missing values and outliers.
- Communicate findings effectively using visualizations.

## Data Cleaning Process
To ensure robust and unbiased analysis, the data cleaning process will involve:

1. **Pipeline for Outlier Detection and Handling**:
   - Identify outliers in key numerical features.
   - Apply appropriate techniques such as capping, removal, or transformation to mitigate their impact.

2. **Handling Missing Data**:
   - Detect missing values across all features.
   - Use techniques such as imputation (mean, median, mode, or advanced methods) or deletion, depending on the context and feature importance.

# Task 2 - Prediction of store sales

## Sub-Tasks

### 2.1 Preprocessing
- Convert non-numeric columns to numeric.
- Handle NaN values.
- Generate new features

### 2.2 Building Models with sklearn Pipelines
- Use tree-based regression algorithms (e.g., `RandomForestRegressor`).
- Implement pipelines for modularity and reproducibility.

### 2.3 Choose a Loss Function
- Select an appropriate loss function and justify the choice.

### 2.4 Post Prediction Analysis
- Explore feature importance.
- Estimate confidence intervals for predictions.

### 2.5 Serialize Models
- Save models with a timestamped filename.

### 2.6 Building Models with Deep Learning
- Prepare time series data (stationary, autocorrelation, supervised format).
- Scale data to range (-1, 1).
- Build an LSTM model using TensorFlow or PyTorch.

# Task-3: Model Serving API

This project implements a REST API to serve a trained machine-learning model for real-time predictions. The API receives input data, preprocesses it, and returns predictions based on the loaded model.

## Framework
The API is built using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

## Prerequisites
- Python 3.7 or later
- The trained machine-learning model
- FastAPI and Uvicorn for serving the API



