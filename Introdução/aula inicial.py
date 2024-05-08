import pandas as pd
import numpy as np

labels = ["a", "b", "c"]
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(pd.Series(labels))
print(pd.Series(data=labels, index=minha_lista))
print(pd.Series(d))

ser1 = pd.Series([1, 2, 3, 4], index = ["EUA", "Rússia", "Alemanha", "Japão"])
ser2 = pd.Series([1, 2, 5, 4], index = ["EUA", "Rússia", "Itália", "Japão"])

print(ser1["Japão"])
print(ser1[["EUA", "Japão"]])