import sys
# Zadanie 1
plik = open('zadanie1.txt', 'w+')
for x in range(0, 31):
    plik.write(str(x*2)+' ')
plik.close()

# Zadanie 2
plik = open('zadanie1.txt', 'r')
zawartosc = plik.readlines()
plik.close()
print(zawartosc)

# Zadanie 3
with open('tekst.txt', 'w+', encoding='utf-8') as plik:
    for x in range(0, 3):
        dane = sys.stdin.readline()
        plik.write(dane)

# Zadanie 4
class NaZakupy:
     """NaZakupy"""

     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
         self.nazwa_produktu = nazwa_produktu
         self.ilosc = ilosc
         self.jednostka_miary = jednostka_miary
         self.cena_jed = cena_jed

     def wyswietl_produkt(self):
         print(self.nazwa_produktu)
         print(self.ilosc)
         print(self.jednostka_miary)
         print(self.cena_jed)

     def ile_produkt(self):
         return str(self.ilosc) + str(self.jednostka_miary)

     def ile_kosztuje(self):
          return self.ilosc * self.cena_jed

produkt = NaZakupy('Pomidory', 4, 'kg', 9.99)
print(produkt.wyswietl_produkt())
print(produkt.ile_produkt())
print(produkt.ile_kosztuje())

# Zadanie 5
class ciag_aryt:
    """Ciag arytmetyczny"""
    def __init__(self, a1, n, r):
        self.a1 = a1
        self.n = n
        self.r = r

    def wyswietl_dane(self):
        for x in range(self.a1, self.n):
            print(x+self.r)


    def pobierz_parametry(self):
        self.a1 = input("Podaj poczatek: ")
        self.a1 = int(self.a1)
        self.n = input("Podaj ilosc: ")
        self.n = int(self.n)
        self.r = input("Podaj roznice: ")
        self.r = int(self.r)

        ciag = []
        for x in range(0, self.n):
            ciag.append(self.a1 + self.r*x)
        return ciag

    def pobierz_elementy(self):
        ciag = []
        self.a1 = input("Podaj ilosc w ciagu: ")
        self.a1 = int(self.a1)
        for x in range (0,self.a1):
            self.n = input("Podaj wartosc: ")
            ciag.append(self.n)
        return ciag

    def policz_sume(self):
        ciag = []
        suma = 0
        for x in range(self.a1,self.n):
            ciag.append(x + self.r)
            suma += x+self.r
        return suma

    def policz_elementy(self):
        ciag = []
        suma = 0
        for x in range(self.a1, self.n):
            ciag.append(x + self.r)
            suma += 1
        return suma

ciag = ciag_aryt(1, 10, 2)
print(ciag.wyswietl_dane())
print(ciag.pobierz_elementy())
print(ciag.pobierz_parametry())
print(ciag.policz_sume())
print(ciag.policz_elementy())

# Zadanie 6
class Robaczek:
    """Robaczek"""
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, kroki):
        self.y = self.y + kroki * self.krok

    def idz_w_prawko(self, kroki):
        self.x = self.x + kroki * self.krok

    def idz_w_dol(self,kroki):
        self.y = self.y - kroki * self.krok

    def idz_w_lewo(self,kroki):
        self.x = self.x - kroki * self.krok

    def gdzie_jestem(self):
        return 'wspolzedne x:' + str(self.x) + ' y:' + str(self.y)


robak = Robaczek(0, 0, 10)
robak.idz_w_gore(4)
robak.idz_w_prawko(2)
robak.idz_w_dol(3)
robak.idz_w_lewo(1)
print(robak.gdzie_jestem())
