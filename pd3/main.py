import random
import ciagi.aryt
import ciagi.geom
# Zadanie 1
A = [1-x for x in range(1, 11)]
print(A)
B = [4**x for x in range(0, 8)]
print(B)
C = [B[x] for x in range(0, 8) if B[x] % 2 == 0]
print(C)

# Zadanie 2
lista1 = []
for x in range(0, 10):
    lista1.append(random.randint(0, 100))
lista1p = [lista1[x] for x in range(0, 10) if lista1[x] % 2 == 0]
print(lista1)
print(lista1p)

# Zadanie 3
art_sp = {'kiwi': 'szt', 'pomidory': 'kg', 'mleko': 'l', 'ser': 'kg', 'baton': 'szt'}
print(art_sp)
art_sp_l = {key: value for key, value in art_sp.items() if value=='szt'}
print(art_sp_l)

# Zadanie 4
def czy_prostokatny (a, b, c):
    if a**2 + b**2 == c**2 :
        return 'Trójkąt jest prostokątny.'
    else :
        return 'Trójkąt nie jest prostokątny.'

print(czy_prostokatny(3, 4, 5))
print(czy_prostokatny(2, 4, 5))

# Zadanie 5
def pole_trapezu (a=2, b=3, h=4):
    return ((a + b)*h)/2

print(pole_trapezu())

# Zadanie 6
def il_el_ciagu6 (a=1, b=4, ile=10):
    for x in range(1, ile+1):
        a = a * b
    return a

print(il_el_ciagu6())

# Zadanie 7
def il_el_ciagu7 (* liczby):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
        for x in liczby:
            iloczyn *= x
        return iloczyn

print(il_el_ciagu7(1,2,3,4))

# Zadanie 8
def kasa(**koszyk):
    suma=0
    for key,value in koszyk.items():
        print("Produkt: {} , Cena: {}".format(key,value),"zł")
    for key,value in koszyk.items():
        suma=suma+value
    print("Suma zakupów: "+ str(suma) + " zł")

kasa(Jablko= 2, Marchew= 1.5, Bulka= 1.8, Ser= 5, Maka= 5.2, Jajka= 6)

# Zadanie 9
print(ciagi.aryt.n_ty_wyraz_a1 (1, 3, 3))
print(ciagi.aryt.n_ty_wyraz_ak (5, 3, 2, 1))
print(ciagi.aryt.n_ty_wyraz_suma(10, 2))
print(ciagi.aryt.suma_p_i_n(1, 11, 2))
print(ciagi.aryt.suma_p(2, 3, 1))

print(ciagi.geom.n_ty_wyraz_a1(1, 3, 3))
print(ciagi.geom.n_ty_wyraz_ak(9, 3, 2, 3))
print(ciagi.geom.suma(2, 1, 3))
print(ciagi.geom.suma(2, 2, 3))
