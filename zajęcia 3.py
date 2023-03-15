import math
# zadanie 1
A = [1-x for x in range(1,11)]
print(A)
B = [4**x for x in range(8)]
print(B)
C = [x for x in B if x%2==0]
print(C)
# zadanie 2
lista1 = [x**2 for x in range(10)]
print(lista1)
lista = [x for x in lista1 if x%2==0]
print(lista)
# zadanie 3
słownik = {"limonka":"kg", "Rum":"butelki", "Ctryny":"kg", "Ziemniaki":"kg", "Chipsy":"pazcki", "konserwa":"puszki"}
produkty = [x for x, y in słownik.items() if y=="kg"]
print(produkty)
# zadanie 4
def trójkąt(a, b , c):
    if a + b > c and a + c > b and b + c > a:
        ak = a**2
        bk = b**2
        ck = c**2
        if ak + bk == ck or ak + ck ==bk or ck + bk == ak:
            return True
        else:
            return False
    else:
        return False
print(trójkąt(3, 4, 5))
# zadanie 5
def trapez(a = 6, b = 5, h = 8):
    pole = (a+b)*h/2
    return pole
print(trapez())
# zadanie 6
def iloczyn(a = 1, b = 4, ile = 10):
    wynik=a
    for x in range(ile):
        wynik*=b
    return wynik
print(iloczyn())
# zadanie 7
def gwiazdka(*liczby):
    if len(liczby)==0:
        return 0
    else:
        wynik=1
        for x in liczby:
            wynik*=x
    return wynik
print(gwiazdka(1,2,3,4))
# zadanie 8
def zakupy(**a):
    suma = 0
    for x, y in a.items():
        suma+=y
    return suma
print(zakupy(korki = 138, klucze = 15, limonka = 2, rum = 50, kola = 6, ziemniaki = 4))
# zadanie 9
def pierwiastek(a):
    try:
        print(math.sqrt(a))
    except:
        print("Mniejsze od zero!!!")
pierwiastek(16)