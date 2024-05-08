import pandas as pd

data = {
    'Classe': ['Júnior', 'Júnior', 'Pleno', 'Pleno', 'Sênior', 'Sênior'],
    'Nome': ['Jorge', 'Carlos', 'Roberta', 'Patrícia', 'Bruno', 'Vera'],
    'Venda': [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)

group = df.groupby('Classe')

print(group.sum(numeric_only=True))
print(group.mean(numeric_only=True))
print(group.min())
print(group.max())

df2 = df.copy()

df2['Venda'] = [150, 432, 190, 230, 410, 155]

df3 = pd.concat([df, df2])
print(df3.groupby(['Classe', 'Nome']).sum(numeric_only=True))