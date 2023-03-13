a = 'napis\ndrugi napis'
print(a)
b = 5
c = 11
print(b, c)
d = 5+3j # liczby zespolone
print(d)
e = c+d
print(e)
f = c//b # dzielenie całkowite
print(f)
g = c % b # modulo
print(g)
h = b**2 # potęgowanie
print(h)
i = b**1/2
j = pow(b, 1/2) # potęgowanie
print(i)
print(j)
print( 'b = b + 2')
b += 2
print(b)
listy = ['a', 4, 5, 6, [1, 2, 3], 5.6]
print(listy)
listy.append(4) # takie push_back()
print(listy)
print(listy[5]) # listy są liczone od zera

# dodać elemnt na wybrane miejsce
listy.insert(4, 5.5)
print(listy)

# usunąć element z listy o danej pozycji
del listy[2]
print(listy)

# usunąć element z listy o danej wartości
listy.remove(6)
print(listy)

# odwrócić elementy listy
print(listy[::-1])

# zrobic sortowanie
lista = [1, 4, 5, 3, 8, 2]
print(sorted(lista))

slownik = {'a': 2, 1:2, 4:'ab', 2:3} # taka mapa
print(slownik)
print(slownik[4])
slownik['klucz'] = 'wartość'
print(slownik)
slownik.pop('klucz') # usuwanie wierszy
print(slownik)
print(slownik.keys())
print(slownik.values())
print('a = %(zb)d'% {"zb":12})
print('a = {}, b = {}'.format(12, 14))

#if warunek1:
    #instrukcja1
    #instrukcja2
#elif warunek2:
    #instrukcja1
    #instrukcja2
#else:
    #instrukcja1
    #instrukcja2

a = input('podaj a: ')
b = input('podaj b: ')
c = input('podaj c: ')
d = input('podaj d: ')

print(a)
print(b)

print(type(a))
print(type(b))

a = int(a)
b = int(b)
c = int(c)
d = int(d)

print(type(a))
print(type(b))
if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print('a = b')
if a==b:
    print("\npodane wartości są równe")
else:
    print("\npodane wartości nie są równe")
if (a>b) & (c>d):
    print('\na większe od b i c większe od d')
else:
    print('\nNIE!!!')

#for element in sekwencja:
    #instrukcja1
    #instrukcja2
#else:
    #instrukcja1
    #instrukcja2
for x in range(1,6,1):
    print(x)
else:
    print('Koniec pętli :)')
for x in listy:
    print(x)
for x in range(len(listy)):
    print(listy[x])

licznik = 0
while licznik !=len(listy):
    print(listy[licznik])
    licznik += 1
liczby = [3, 4, 5, 7, 2, 9]
a = int(input('Podaj a: '))
licznik = 0
while licznik != len(liczby):
    if a - liczby[licznik] == 0:
        print('{} - {} = 0'.format(a, liczby[licznik]))
        break
    licznik += 1
liczby1 = [ 1, 2, 2, 2, 4, 5, 6]
licznik1 = 0
while licznik1 != len(liczby1):
    if liczby1[licznik1] == 2:
        liczby1.pop(licznik1)
    else:
        licznik1 += 1
for x in liczby1:
    print(x)