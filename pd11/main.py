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


# Zadanie 4
df = pd.read_csv(r'C:\Users\local\Desktop\zadania\python\2022.05.11\pd11\iris.data', sep=',', decimal='.',
                 names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
df.to_csv(r'C:\Users\local\Desktop\zadania\python\2022.05.11\pd11\iris.csv', index=None)
print(df)
x=pd.assign(('sepal length')
y='sepal width'
