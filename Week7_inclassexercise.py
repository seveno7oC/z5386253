import pandas as pd
#exercise 1&2
df = pd.DataFrame({'col1': range(10), 'col2': range(10, 20)}, index=list('acgfhibdje'))
print(df)

df.sort_index(inplace=True)
x = df.loc['b':'e', 'col1']
print(x)

x = df.loc[['b', 'd', 'f', 'j'], ['col1']]
print(x)



#exercise 3
df3 = pd.DataFrame({'col1': range(0, 20), 'col2': range(20, 40), 'col': range(40, 60)})
print(df3)

rows = list(range(0, len(df3), 2))
r = df3.iloc[rows,[1]]
print(r)