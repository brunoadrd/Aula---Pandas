import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(5,4), index=["A", "B", "C", "D", "E"], columns="W X Y Z".split())

print(df["W"])
print(df[["W"]])

df["new"] = df["W"] + df["Y"]

print(df[["new"]])
print(df.drop("new", axis=1)) #axis = 1 -> Coluna, 0 -> Linha
print(df.drop("new", axis=1, inplace=True)) #inplace substitui a tabela original
print(df.loc[["A", "B"]])
print(df.iloc[0,3])

print(df[df > 0])
print(df[df["Y"] > 0])
print(df[(df["Y"] > 0) & (df["W"] > 0)])
df.index
df.columns
df.reset_index(inplace=True)
df.set_index("index", inplace=True)