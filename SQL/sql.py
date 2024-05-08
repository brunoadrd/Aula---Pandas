import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')
c = conn.cursor()

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'

#df_data.to_sql('data', conn, index_label='index_name')

#c.execute('CREATE TABLE products (product_id, product_name, price)')
#conn.commit()

#c.execute('DROP TABLE products')
#c.execute('DROP TABLE data')
#conn.commit()

#c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')
#c.execute('DROP TABLE products')
#conn.commit()

#c.execute('''INSERT INTO products (product_id, product_name, price) VALUES
#    (1, 'Computer', 800),
#    (2, 'Printer', 200),
#    (3, 'Tablet', 300)
#''')
#conn.commit()

#df_data2 = df_data[::-2]
#df_data2.to_sql('data', conn, if_exists='append')

c.execute('SELECT A, B, C FROM data WHERE A > 200 AND B > 100')
df = pd.DataFrame(c.fetchall())
print(df)

query = 'SELECT * FROM data'
df = pd.read_sql(query, con=conn, index_col='index_name')
print(df)

c.execute("UPDATE data SET A = 230, B = 355 WHERE index_name='b'")
conn.commit()

c.execute("DELETE FROM data WHERE index_name='b'")
conn.commit()

