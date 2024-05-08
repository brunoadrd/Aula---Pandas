import pandas as pd

df1 = pd.read_csv("Dataserts/exemplo.csv", sep=",", decimal=".")

df1.info() # Dtype = float64? Se sim, reconheceu corretamente

df1.to_csv("exemplo_saida.csv", sep=";", decimal=",")