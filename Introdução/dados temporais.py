import pandas as pd

numero_de_dias = 100
datas = pd.date_range(start='1/1/2021', periods=numero_de_dias)

df = pd.DataFrame(range(numero_de_dias), columns=["Number"], index=datas)

print(df[df.index.day == 10])