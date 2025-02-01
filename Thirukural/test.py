import pandas as pd
df = pd.read_csv("Thirukural1.csv",delimiter=",")
df.head()
df.columns = df.columns.str.strip()
print(df.columns)