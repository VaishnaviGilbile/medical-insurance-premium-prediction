
import pandas as pd

class InsurancePredictor:
    def __init__(self):
        # Load the insurance dataset from a CSV file
        self.data = self.load_data()

    def load_data(self):
        # Replace 'your_insurance_dataset.csv' with the actual path to your CSV file
        file_path = 'insurance.csv'
        data = pd.read_csv(insurance.csv)
        return data

    def predict_insurance(self, age, sex, bmi, children, smoker, region):
        # Use self.data to perform predictions based on the loaded dataset
        # This is just a dummy example
        prediction = f"Predicted Insurance Cost: ${int(age) * 10 + int(bmi) * 5}"
        return prediction
