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
print(df[df['Plec'] == 'M'].sort_values('Liczba', ascending=False).head(1))
print(df[df['Plec'] == 'K'].sort_values('Liczba', ascending=False).head(1))


# ZADANIE 3
df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal='.')
print(df)
# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
print(df['Sprzedawca'].unique())

# 5 najwyższych wartości zamówień
print(df.sort_values('Utarg', ascending=False).head(5))

# ilość zamówień złożonych przez każdego sprzedawcę
print(df.groupby('Sprzedawca').size())

# sumę zamówień dla każdego kraju
print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
# print(df.groupby('Kraj').size())

# sumę zamówień dla roku 2005, dla sprzedawców z Polski
rok2005 = df[((df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
print(rok2005)

# średnią kwotę zamówienia w 2004 roku,

rok2005 = df[((df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31'))]
print(rok2005)

# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
rok2004.to_csv('plik1.csv', index=False)
rok2005.to_csv('plik2.csv', index=False)
