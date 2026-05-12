import pandas as pd
filepath = 'C:/Users/jthiuri/datacore-website/data/raw/finance.csv'
finance = pd.read_csv(filepath)
print(finance.head())