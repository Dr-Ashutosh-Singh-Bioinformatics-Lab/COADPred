# COADPred/Validation.py

import os
import pandas as pd
import joblib

def predict(df, model_type='svc'):
    # List of selected genes
    selected_genes = ['STMN4', 'CLCA4', 'GUCA2B', 'NFE2L3', 'CDH3', 'GLP2R', 'TRIP13', 'MMP11', 'SEC14L2', 'SLCO4A1', 'TRIB3',  'SGCG', 'CEMIP', 'STMN2', 'GRIN2D', 'RERGL', 'MSX2', 'INHBA', 'PLP1', 'PCSK2', 'PYY', 'GLTP', 'PDX1',  'BEST4', 'RSPO2', 'FAM135B', 'BMP3', 'LRP8', 'SIM2', 'IL6R', 'CLDN1', 'ESM1', 'FOXQ1', 'VWA2', 'KRT80',  'SCARA5', 'GFRA2', 'CA7', 'CST1', 'VSTM2A', 'EPHX4', 'ETV4', 'CPNE7', 'SLC17A8', 'TMIGD1', 'OTOP3',  'OTOP2', 'NPY2R', 'TMEM72', 'SFTA2', 'FAM180B', 'S100A2', 'EPOP', 'BLACAT1']
 # Select features from dataframe
    df_selected = df[selected_genes]
    
    # Construct model path
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_type.lower()}.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model '{model_type}' not found. Ensure the model file exists at {model_path}.")
    
    # Load the model
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(df_selected)
    
    # Add predictions to dataframe
    df['Prediction'] = ['Cancer' if pred == 1 else 'Normal' for pred in y_pred]
    
    # Save predictions to CSV file
    df.to_csv('predictions.csv', index=False)
    
    # Print diagnosis
    count_cancer = y_pred.sum()
    count_normal = len(y_pred) - count_cancer
    percentage_cancer = count_cancer / len(y_pred)
    percentage_normal = count_normal / len(y_pred)
    
    if percentage_cancer > 0.6:
        print(f"Colon Adenocarcinoma patient detected, {percentage_cancer*100:.2f}%")
    else:
        print(f"Normal patient detected, {percentage_normal*100:.2f}%")

