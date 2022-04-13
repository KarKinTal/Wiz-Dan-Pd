import numpy as np
# Zadanie 1
# Utwórz dwie macierze 1x3 różnych wartości
# a następnie wykonaj operację mnożenia.

a = [1, 3, 5]
b = [2, 4, 6]
ma = np.array(a)
mb = np.array(b)
mw = ma * mb
print(mw)

# Zadanie 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe
# wartości dla każdej kolumny i każdego rzędu.

a = np.array([[3, 3, 2], [4, 5, 3], [6, 2, 1]])
b = np.array([[3, 3, 2, 1], [4, 5, 3, 6], [6, 2, 1, 4], [1, 4, 5, 2]])
print(a)
print(a.min(axis=0))
print(a.min(axis=1))
print('')
print(b)
print(b.min(axis=0))
print(b.min(axis=1))



# Zadanie 3
# Wykorzystaj macierze z zadania pierwszego
# i wykonaj iloczyn macierzy.

a = [1, 3, 5]
b = [2, 4, 6]
ma = np.array(a)
mb = np.array(b)
w = ma.dot(mb)
print(w)

# Zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich
# będzie zawierała liczby całkowite, a druga liczby rzeczywiste.
# Następnie wykonaj na nich operację mnożenia.

a = [1, 3, 5]
b = [2.25, 4.5, 6.75]
ma = np.array(a)
mb = np.array(b)
mw = ma * mb
print(mw)

# Zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus
# dla każdej z jej wartości i zapisz do zmiennej “a”.

m = np.array([[1, 2, 3], [9, 8, 7]])
print(m)
a = np.sin(m)
print(a)
print('')

# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz
# cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.

m = np.array([[4, 3, 2], [6, 7, 8]])
print(m)
b = np.cos(m)
print(b)
print('')

# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej
# do zmiennych a i b.
w = a + b
print(w)

# Zadanie 8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

a = np.arange(9).reshape(3, 3)
print(a)
for b in a:
    print(b)

# Zadanie 9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element
# korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())
a = np.arange(9).reshape(3, 3)
print(a)
for b in a.flat:
    print(b)

# Zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy
# możliwości i dlaczego?

a = np.arange(81).reshape(9, 9)
print(a)
b = a.reshape((3, 27))
print(b)
c = a.reshape((27, 3))
print(c)
d = a.reshape((1, 81))
print(d)
e = a.reshape((81, 1))
print(e)


# Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4.
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą
# z nich i wyświetl wyniki. Czy są identyczne?
a = np.arange(12)
a1 = a.reshape(3, 4)
a2 = a.reshape(4, 3)
a3 = a.reshape(2, 6)
print(a1.ravel())
print(a2.ravel())
print(a3.ravel())