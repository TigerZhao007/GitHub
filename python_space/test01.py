
import pandas as pd

a = [1,2,3]
a1 = (1,2,3)
b = [2,3]
df = pd.DataFrame({'a':a, 'b':a})

a[1] in b
[x in b for x in a]

df.a
type(df.a)
type(a1)
df.a.isin(b)

a.isin(b)


