import numpy as np
# inicjalizacja tabeli
a = np.array([[0, 1], [2,3]])
print(a)
# lub drugi sposób
a = np.arange(2, 5, 0.1)
print(a)
# wprowadzenie typu zmiennej tablicy (nie jej elementów)
print(type(a))
# sprawdzenie typu danych tablicy
print(a.dtype)
# inicjalizacja tablicy z konkretnym typem danych
a = np.arange(2, dtype = 'int64')
print(a.dtype)
# zapisywanie kopii tablicy jako tablicy z innym typem danych
b = a.astype(("float"))
print(b)
print(b.dtype)
# wyisanie rozmiaru tablicy
print(b.shape)
# mozna też sprawdzić ilość wymiarów tablicy
print(a.ndim)
# sprawdzenie tablicy wielowymiarowej moze wyglądać tak
# przekazywanym elementem do funkcji array jest obiekt.
# może to być pythonowa lista
m = np.array([np.array(2), np.array(2)])
print(m.shape)
# ponownie typem jest ndarray
print(type(m))

zera = np.zeros((5, 5))
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)
# warto sprawdzić jaki jest domyślny typ danych takich tablic
print(zera.dtype)
print(jedynki.dtype)
# można również stworzyć "pusta" macież o podanych wartościach z losowymi wartościami
pusta = np.empty((2,2))
print(pusta)

macierz = np.array([[12, 11], [2, 1]])
print(macierz)
# do elementów tablicy mozemy odwołać się tak jak do elementów macierzy
poz_1 = macierz[1, 1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)
# podobnie działa fynkcja linspace, które działanie jest podobne do array
liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)
# a teraz możemy utworzyć dwie macierze najpierw wartość
z = np.indices((5, 3))
print(z)
print(z[0][1][2])
# macierze podobne jak w MATLAB diag xd
mat_diag = np.diag([a for a in range(5)], 1)
print(mat_diag)
# numpy jest w stanie stworzyć tablicę jednowymiarową
z = np.fromiter(range(5), dtype='int32')
print(z)

znaki = b'ogolna'
z1 = np.frombuffer(znaki, dtype='S1')
print(z1)
z2 = np.frombuffer(znaki, dtype='S2')
print(z2)

znaczki = 'ogolna'
z3 = np.array(list(znaczki))
z4 = np.array(list(znaczki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaczki,dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(7,2)
print(a[s])
# lub tak jak w listach
print(a[2:7:2])
# lub tak
print(a[1:])
print(a[2:5])
mat = np.arange(25)
mat = mat.reshape((5,5))
print(mat)
print(mat[1:]) # od drugiego wiersza
print(mat[:, 1:2]) # druga kolumna jako wektor
print(mat[:,-1]) # ostatnia kolumna
print(mat[2:5, 1:3])
print(mat[:, [2,4]])
x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(x)
rows = np.array([[0,0], [3,3]])
cols = np.array([[0,2], [0,2]])
y = x[rows, cols]
print(y)