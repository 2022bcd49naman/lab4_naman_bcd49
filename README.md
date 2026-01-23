# Wine Quality Prediction - Machine Learning Project

A machine learning project that predicts wine quality using Lasso regression. This project implements a complete ML pipeline including data preprocessing, model training, evaluation, and automated CI/CD workflows.

## 📋 Project Information

- **Author:** Naman Omar
- **Roll Number:** 2022BCD0049
- **Course:** CSS426 - Lab 4

## 🎯 Overview

This project trains a Lasso regression model to predict wine quality based on various wine characteristics. The model is trained on a wine quality dataset and evaluated using Mean Squared Error (MSE) and R² Score metrics.

## 🏗️ Project Structure

```
lab2_bcd49/
├── data/
│   └── wine_quality.csv          # Dataset file
├── output/
│   ├── model/
│   │   └── model.pkl             # Trained model (generated)
│   └── results/
│       └── metrics.json          # Evaluation metrics (generated)
├── .github/
│   └── workflows/
│       └── train.yaml            # GitHub Actions CI/CD workflow
├── train.py                      # Main training script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Setup

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/2022bcd49naman/lab2_bcd49
cd lab2_bcd49
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running the Training Script

To train the model locally, simply run:

```bash
python train.py
```

The script will:

1. Load the wine quality dataset from `data/wine_quality.csv`
2. Preprocess the data using StandardScaler
3. Split the data into training and testing sets (80/20)
4. Train a Lasso regression model with alpha=0.1
5. Evaluate the model and print metrics (MSE and R² Score)
6. Save the trained model to `output/model/model.pkl`
7. Save evaluation metrics to `output/results/metrics.json`

### Output

After running the training script, you'll find:

- **Model:** `output/model/model.pkl` - The trained Lasso regression model
- **Metrics:** `output/results/metrics.json` - Evaluation results in JSON format

## 📦 Dependencies

The project requires the following Python packages:

- `pandas` - Data manipulation and analysis
- `scikit-learn` - Machine learning library
- `joblib` - Model serialization
- `numpy` - Numerical computing

All dependencies are listed in `requirements.txt`.

## 🤖 Model Details

- **Algorithm:** Lasso Regression
- **Regularization Parameter (alpha):** 0.1
- **Preprocessing:** StandardScaler (feature scaling)
- **Train-Test Split:** 80% training, 20% testing
- **Random State:** 42 (for reproducibility)

## 🔄 CI/CD Pipeline

This project includes a GitHub Actions workflow (`.github/workflows/train.yaml`) that:

- Automatically runs training on push or pull request to main branch
- Sets up Python 3.10 environment
- Installs dependencies
- Runs the training script
- Generates a job summary with experiment results
- Uploads model and results as artifacts

## 📊 Evaluation Metrics

The model is evaluated using:

- **MSE (Mean Squared Error):** Measures the average squared difference between predicted and actual values
- **R² Score (Coefficient of Determination):** Measures how well the model explains the variance in the target variable

## 📝 Notes

- The dataset should be placed in the `data/` directory before running the training script
- The `output/` directory structure is automatically created if it doesn't exist
- Model and results are saved for future use and deployment

## 📄 License

This project is part of a course assignment (CSS426 Lab 4).
