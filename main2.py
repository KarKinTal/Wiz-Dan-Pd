import sys as system
import math
# zadanie 1
sporty = ['snooker', 'szachy', 'krav-maga', 'pływanie', 'joga']
sporty.reverse()
sporty.append('siatkówka')
sporty.append('piłka nożna')
print(sporty)

# zadanie 2
skroty = {'nr': 'numer', 'zw': 'zaraz wracam', 'nwm': 'nie wiem', 'ss': 'screenshot', 'np': 'na przykład'}
print(skroty)
 
# zadanie 3
gry = {1: 'Gris', 2: 'The binding of Isaac', 3: 'Return of the Obra Dinn', 4: 'Elsword', 5: 'Children of Morta'}
print(len(gry.keys()))

# zadanie 4
zdanie = input('Napisz zdanie:\n')
print(zdanie.count('a'))

# zadanie 5
system.stdout.write('Podaj liczby: ')
system.stdout.write('a = ')
a = system.stdin.readline()
system.stdout.write('b = ')
b = system.stdin.readline()
system.stdout.write('c = ')
c = system.stdin.readline()
system.stdout.write(str(int(a)**int(b) + int(c)))

# zadanie 6
print('\nPodaj liczby: ')
l1 = int(input('1) '))
l2 = int(input('2) '))
l3 = int(input('3) '))
if l1 >= l2:
    if l1 >= l3:
        print('Liczba %(l)d jest największa' % {'l': l1})
    elif l3 >= l1:
        print('Liczba %(l)d jest największa' % {'l': l3})
else:
    if l2 >= l3:
        print('Liczba %(l)d jest największa' % {'l': l2})
    elif l3 >= l2:
        print('Liczba %(l)d jest największa' % {'l': l3})

# zadanie 7
liczby = [1, 2, 3.0, 4.0, 5]
for i in range(0, len(liczby), 2):
    liczby.insert(i, liczby[i] * liczby[i])
print(liczby)

# zadanie 8
parzyste = []
licznik = 1
n = 0
while licznik <= 10:
    liczba = int(input(str(licznik) + ') '))
    if (liczba % 2) == 0:
        parzyste.append(liczba)
    licznik += 1
print(parzyste)

# zadanie 9
licz = input('Podaj liczbe: ')
try:
    print(math.sqrt(int(licz)))
except ValueError:
    print('Nie da się obliczyć pierwiastka z liczby ujemnej.')
