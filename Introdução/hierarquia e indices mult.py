import pandas as pd
from numpy.random import randn

outside = "G1 G1 G1 G2 G2 G2".split()
inside = [1, 2, 3, 1, 2, 3]

hier_index = list(zip(outside, inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2), index=hier_index, columns=['A', 'B'])
print(df.loc['G1'].loc[1])
df.index.names = ['Grupo', 'Número']
print(df)

print(df.xs(1, level='Número'))