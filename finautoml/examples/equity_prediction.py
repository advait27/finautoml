"""
Example script for equity price prediction using finance_automl.
"""
from finance_automl import AutoML

# Placeholder for loading data
def load_data():
    # Replace with actual data loading logic
    X, y = None, None
    return X, y

if __name__ == "__main__":
    X, y = load_data()
    automl = AutoML()
    automl.run(X, y)
