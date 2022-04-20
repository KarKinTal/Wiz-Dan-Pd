import numpy as np
import pandas as pd

# ZADANIE 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
print('')

# ZADANIE 2
# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print(df[df['Liczba'] > 1000])

# tylko rekordy gdzie nadane imię jest takie jak Twoje
print(df[df['Imie'] == 'KAROLINA'])

# sumę wszystkich urodzonych dzieci w całym danym okresie,
print(df.agg({'Liczba': ['sum']}))

# sumę dzieci urodzonych w latach 2000-2005
print(df[((df.Rok >=2000) & (df.Rok <=2005))].agg({'Liczba': ['sum']}))

# sumę urodzonych chłopców i dziewczynek,
print(df.groupby('Plec').agg({'Liczba': ['sum']}))

# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),

print(df[df['Plec'] == 'M'].groupby(['Rok']).head(1))
print(df[df['Plec'] == 'K'].groupby(['Rok']).head(1))

# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
print(df[df['Plec'] == 'M'].sort_values('Liczba', ascending=False).head(6))

# ZADANIE 3