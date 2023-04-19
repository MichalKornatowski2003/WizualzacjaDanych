import numpy as np

# zad 1
def zad1():
    a = np.array([1, 2, 3])
    b = np.array([4, 8, 12])
    print(a)
    print(b)
    print(a*b)
#zad1()

# zad 2
def zad2():
    a = np.array([[3, 4, 5], [4, 6, 8], [7, 6, 8]])
    print(a)
    ka = np.min(a, axis=1)
    wa = np.min(a, axis=0)
    print(ka)
    print(wa)
    b = np.array([[3, 4, 5, 8], [4, 6, 8, 2], [7, 6, 8, 4], [4, 5, 2, 6]])
    print(a)
    kb = np.min(b, axis=1)
    wb = np.min(b, axis=0)
    print(kb)
    print(wb)
#zad2()

# zad 3
def zad3():
    a = np.array([1, 2, 3])
    b = np.array([4, 8, 12])
    iloczyn = np.dot(a, b)
    print(iloczyn)
#zad3()

# zad 4
def zad4():
    a = np.array([1, 2, 3])
    b = np.array([4.8, 8.3, 12.2])
    c = a*b
    print(c)
#zad4()

# zad 5
def zad5():
    matrix = np.array([[2, 4, 8], [4.8, 16, 30]])
    a = np.sin(matrix)
    print(a)
#zad5()

# zad 6
def zad6():
    matrix = np.array([[2, 4, 8], [4.8, 16, 30]])
    b = np.cos(matrix)
    print(b)
#zad6()

# zad 7
def zad7():
    matrix = np.array([[2, 4, 8], [4.8, 16, 30]])
    a = np.sin(matrix)
    b = np.cos(matrix)
    suma = a + b
    print(suma)
#zad7()

# zad 8
def zad8():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    for rząd in matrix:
        print(rząd)
#zad8()

# zad 9
def zad9():
    a = np.arange(9).reshape(3,3)
    for i in a.flat:
        print(i)
#zad9()

# zad 10
def zad10():
    a = np.arange(81)
    print(a)
    a = np.arange(81).reshape(9, 9)
    print(a)
    a = np.arange(81).reshape(3, 27)
    print(a)
    a = np.arange(81).reshape(27, 3)
    print(a)
    a = np.arange(81).reshape(1, 81)
    print(a)
    a = np.arange(81).reshape(81, 1)
    print(a)
#zad10()

# zad 11
def zad11():
    matrix = np.arange(12)
    a = matrix.reshape(3, 4)
    b = matrix.reshape(4, 3)
    c = matrix.reshape(2, 6)
    print(a.ravel())
    print(b.ravel())
    print(c.ravel())
#zad11()