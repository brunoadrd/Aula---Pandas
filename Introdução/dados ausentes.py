import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3]
})

print(df.dropna(axis=0, thresh=2))
print(df.fillna(''))
print(df['A'].fillna(value=df['A'].mean()))
print(df.ffill()) #bfill faz o inverso