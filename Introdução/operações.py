import pandas as pd

def comp(x):
    return x ** 2 + 3

df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [444, 555, 666, 444],
    'col3': ['abc', 'def', 'ghi', 'xyz']
})

print(df.head())
print(df.info())
print(df.memory_usage())

df['col2'].unique()
df['col2'].nunique()
df['col2'].value_counts()

df['col1_calc'] = df['col1'].apply(comp)
df['col1'].apply(lambda x: x ** 2 + 3)

print(df[df['col2'] == 444]['col1'].sum())

data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
'B':['one', 'one', 'two', 'two', 'one', 'one'],
'C': ['x', 'y', 'x', 'y', 'x', 'y'],
'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
dict_map = {
    'one': '1',
    'two': '2'
}

df['E'] = df['B'].map(dict_map)

print(df)

print(df.pivot_table(index='A', columns='B', values='D')) #faz média