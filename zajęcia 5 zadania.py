import numpy as np
# zad 1
zad1 = np.arange(0,81,4)
print(zad1)
# zad 2
zad2 = np.array([4.0, 5.2, 6.5, 7.7])
print(zad2)
zad2p = zad2.astype('int32')
print(zad2p)
# zad 3
def zad3():
    n = int(input("Podaj n:"))
    a = np.arange(n**2)
    a = np.power(2, a)
    a = a.reshape((n, n))
    print(a)
zad3()
# zad 4
