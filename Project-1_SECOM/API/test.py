import requests
import pandas as pd
import json

try:
    data = pd.read_csv(r"C:\Users\dashi\Documents\Semiconductor-Projects\Project-1_SECOM\API\secom_merged.csv")
    print(data.head())
except FileNotFoundError:
    print("CSV file not found. Please check the file path.")
    
    
