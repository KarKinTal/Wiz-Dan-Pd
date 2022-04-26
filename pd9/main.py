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
print(pd.unique(df['Sprzedawca']))

# 5 najwyższych wartości zamówień
print(df.sort_values(by='Utarg', ascending=False).head(5))

# ilość zamówień złożonych przez każdego sprzedawcę
print(df['Sprzedawca'].value_counts(ascending=False))

# sumę zamówień dla każdego kraju
print(df.where((df['Data zamowienia'] > '20050101') &
               (df['Data zamowienia'] < '20051231') & (df['Kraj']=='Polska')).count())

# sumę zamówień dla roku 2005, dla sprzedawców z Polski
print(df.where((df['Data zamowienia'] > '20040101') &
               (df['Data zamowienia'] < '20041231') & (df['Utarg'])).mean())

# średnią kwotę zamówienia w 2004 roku,
a = df.where((df['Data zamowienia'] > '20040101') & (df['Data zamowienia'] < '20041231') & (df['Utarg'])).mean()
b = df.where((df['Data zamowienia'] > '20050101') &
             (df['Data zamowienia'] < '20051231') & (df['Kraj'] == 'Polska')).count()

# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
a.to_csv('plik1.csv', index=False)
b.to_csv('plik2.csv', index=False)
