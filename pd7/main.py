import numpy as np
# # Zadanie 1
# zad1 = np.arange(4, 81, 4)
# print(zad1)

# # Zadanie 2
# zad2 = np.arange(5, dtype = 'float64')
# print(zad2)
# print(zad2.dtype)
# zad2_k = zad2.astype('int')
# print(zad2_k)
# print(zad2_k.dtype)

# # Zadanie 3
# def zadanie3 (n=3):
#     tab = np.array([2**a for a in range(n*n)])
#     return tab.reshape((n,n))
# n = input('Podaj n: ')
# n = int(n)
# print(zadanie3(n))

# # Zadanie 4
# def zadanie4 (liczba, ilosc):
#     return np.logspace (1, ilosc, num=ilosc, base=liczba)
#
# print(zadanie4(2, 3))

# # Zadanie 5
# def zadanie5(n):
#     a = np.arange(n, -1, -1)
#     diag = np.diag(a, 2)
#     return diag
#
# print(zadanie5(4))

# # Zadanie 6
# malina = np.array(list('malina'))
# mrowka = np.array(list('mrówka'))
# armata = np.array(list('armata'))
# armata = np.flip(armata)
# 
# wykreslanka = np.zeros((6,6), dtype='str')
# 
# print(wykreslanka)
# wykreslanka[:, 0] = mrowka
# wykreslanka[5,::-1] = armata
# for a in range(5):
#     wykreslanka[a,a] = malina[a]
# print(wykreslanka)

# # Zadanie 7
# def zadanie7(n):
#     mac = np.zeros((n, n), dtype='int32')
#     mac += np.diag([2 for _ in range(n)])
#     for i in range(1, n):
#         mac += np.diag([2+(2*i) for _ in range(n-i)], k=i)
#         mac += np.diag([2+(2*i) for _ in range(n-i)], k=-i)
#     print(mac)
# zadanie7(3)

# # Zadanie 8
# def zadanie8 (tab, kierunek='poziomo'):
#     print(tab)
#     if kierunek == 'poziomo':
#         if tab.shape[0] % 2 != 0:
#             print("Tablica posiada nieprzystą liczbę wierszy")
#             return
#         p1 = tab[0:int(tab.shape[0]/2), :]
#         p2 = tab[int(tab.shape[0]/2):, :]
#         print("***** część 1 *****")
#         print(p1)
#         print("***** część 2 *****")
#         print(p2)
#     elif kierunek == "pionowo":
#         if tab.shape[1] % 2 != 0:
#             print("Tablica posiada nieprzystą liczbę kolumn")
#             return
#         p1 = tab[:, 0:int(tab.shape[1]/2)]
#         p2 = tab[:, int(tab.shape[1] / 2):]
#         print("***** część 1 *****")
#         print(p1)
#         print("***** część 2 *****")
#         print(p2)
# zadanie8 (np.arange(36).reshape((6,6)), kierunek='pionowo')

# # Zadanie 9
# def n_ty_wyraz(a1, n, r):
#    return a1 + (n-1)*r
# 
# zadanie9 = np.ones(25, dtype='int32')
# print(zadanie9)
# for a in range(0, 25, 1):
#     element = n_ty_wyraz(4, a+1, 4)
#     zadanie9[a] = element
# 
# zadanie9 = zadanie9.reshape((5, 5))
# print(zadanie9) 
