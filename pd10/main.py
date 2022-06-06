import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
print('')

# Zadanie 1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych
# dzieci dla każdego roku.
zadanie1 = df.groupby('Rok').agg({'Liczba':['sum']})
zadanie1.plot(ylabel='Liczba urodzeń', xlabel='Rok', rot=0, legend=False, title='Liczba urodzonych dzieci',
              xticks=(pd.Series(range(2000, 2018))), fontsize=7)
plt.show()

# Zadanie 2
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych
# chłopców i dziewczynek z całego zbioru.
zadanie2 = df.groupby('Plec').agg({'Liczba': ['sum']})
zadanie2.plot(kind='bar', ylabel='Liczba urodzonych', xlabel='Pleć', rot=0, legend=False,
              title='Liczba urodzonych dziewczynek i chłopców', fontsize=10)
plt.xticks([0, 1], labels=['Dziewczynki', 'Chłopcy'])
plt.yticks(np.arange(0, 4100000, step=500000))
plt.show()

# Zadanie 3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych
# chłopców i dziewczynek w ostatnich 5 latach z datasetu.
zadanie3 = df[(df['Rok'] >= 2012) & (df['Rok'] <= 2017)].groupby('Plec').agg({'Liczba': ['sum']})
wykres = zadanie3.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
plt.legend()
plt.show()


# Zadanie 4
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień
# przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
df = pd.read_csv('zamowienia.csv', delimiter=';')
policzone = df.groupby('Sprzedawca').size()
policzone.plot.bar()
plt.ylabel("liczba zamówień")
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
plt.title('Ilość zamówień sprzedawców')
plt.show()


