import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# # Zadanie 1
# x = np.arange(1,21,1)
# y = 1/x
# plt.plot(x, y, label="f(x)= 1/x")
#
# plt.xlim([1, len(x)])
# plt.ylim([0,1])
#
# plt.xlabel('x')
# plt.ylabel('f(x)')
#
# plt.legend()
#
# plt.show()


# # Zadanie 2
# x = np.arange(1,21,1)
# y = 1/x
# plt.plot(x, y, 'g^:', label="f(x)= 1/x", )
#
# plt.xlim([1, len(x)])
# plt.ylim([0,1])
#
# plt.xlabel('x')
# plt.ylabel('f(x)')
#
# plt.legend()
# plt.title("Wykres funkcji f(x) dla x[1,20]")
#
# plt.show()


# # Zadanie 3
# x = np.arange(0, 30, 0.1)
# ys = np.sin(x)
# yc = np.cos(x)
#
# plt.plot(x, ys, label="f(x) = sin(x)")
# plt.plot(x, yc, label="f(x) = cos(x)")
#
# plt.xlabel('x')
# plt.ylabel('f(x)')
#
# plt.legend(loc='upper right')
# plt.title("Wykres funkcji f(x) dla x[1,20]")
#
# plt.show()


# # Zadanie 4
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# colors = np.random.randint(0, 50, len(df.index))
# scale = np.abs(df['sepal length'] - df['sepal width'])
# 
# plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()

# # Zadanie 5
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# plt.subplot(1, 3, 1)
# grouped = df.groupby('Plec')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba narodzonych dzieci')
# 
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
# mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
# plt.plot(x, kobiety, label="Kobiety")
# plt.plot(x, mezczyzni, label="Mężczyźni")
# plt.xlabel('Rok')
# 
# plt.subplot(1, 3, 3)
# x = df['Rok'].unique()
# y = df.groupby('Rok').agg('Liczba').sum()
# plt.bar(x, y)
# plt.xlabel('Rok')
# 
# plt.subplots_adjust(wspace=0.85)
# plt.show()

# Zadanie 6
# df = pd.read_csv('zamowienia.csv', sep=';')
# policzone = df.groupby('Sprzedawca')['Utarg'].sum()
# print(policzone)
# 
# explode = [0.0 for n in range(len(policzone.index))]
# 
# explode[np.random.randint(0, len(policzone.index))] = 0.2
# wedges, texts, autotext = plt.pie(x=policzone, labels=policzone.index,
#                                   autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), explode=explode, shadow=True)
# plt.title("Procentowy udział kwot zamówień sprzedawców")
# plt.show()
