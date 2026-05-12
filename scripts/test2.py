import pandas as pd
filepath = 'C:/Users/jthiuri/datacore-website/data/raw/finance2.csv'
finance2 = pd.read_csv(filepath)
print(finance2.head())