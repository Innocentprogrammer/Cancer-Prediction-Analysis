import pandas as pd
cancer = pd.read_csv('Cancer.csv')
cancer = cancer.drop(['Unnamed: 32', 'id'], axis=1)
cancer.to_csv('Cancer_Cleaned.csv', index=False)
