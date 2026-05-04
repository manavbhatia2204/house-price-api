# House Price Prediction API

## Project Overview
This project predicts house prices using Machine Learning and exposes the trained model through a FastAPI REST API.

Users can send house details such as living area, overall quality, and garage capacity, and the API returns a predicted house price.

---

## Features
- Data preprocessing using Pandas
- Handled missing values
- Converted categorical features using one-hot encoding
- Trained Decision Tree model
- Trained Random Forest model
- Hyperparameter tuning experiments
- Saved trained model using Joblib
- Built REST API using FastAPI
- Added input validation using Pydantic
- Real-time prediction endpoint
- Deployed-ready architecture

---

## Tech Stack
- Python
- Pandas
- Scikit-learn
- FastAPI
- Pydantic
- Uvicorn
- Joblib
- Git
- GitHub
- Render

---

## Dataset
Dataset used:
Kaggle House Prices Dataset

File used:
- train.csv

Target Variable:
- SalePrice

---

## Machine Learning Workflow
1. Load dataset
2. Handle missing values
3. Convert categorical variables
4. Train-test split
5. Train Decision Tree model
6. Train Random Forest model
7. Compare MAE scores
8. Tune model parameters
9. Save best model
10. Build API layer

---

## API Endpoints

## Sample Input

```json
{
  "GrLivArea": 1500,
  "OverallQual": 7,
  "GarageCars": 2
}

## Sample Output

{
  "predicted_price": 149111.58
}

### GET /
Checks whether API is running

Example Response:

```json
{
  "message": "House Price Prediction API is running"
}

## Live Demo
API URL: https://house-price-api-ob1n.onrender.com

Swagger Docs:
https://house-price-api-ob1n.onrender.com/docs