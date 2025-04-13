import joblib
import os
import numpy as np

# Get the directory of the current script
model_dir = os.path.dirname(__file__)

# Construct the full path to the model and scaler files
model_path = os.path.join(model_dir, '../pcos_model/pcos_model.pkl')
scaler_path = os.path.join(model_dir, '../pcos_model/scaler.pkl')

# Load the trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def predict_pcos(features):
    # Scale the features using the pre-trained scaler
    scaled_features = scaler.transform(features)
    
    # Make the prediction using the pre-trained model
    prediction = model.predict(scaled_features)
    
    return prediction[0]  # Return the prediction (1 or 0)
