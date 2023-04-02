import math
def zad1():
    try:
        a = int(input("Podaj liczbę a: "))
        b = int(input("Podaj liczbę b: "))
    except ValueError:
        print("Wszystkie dane powinny być liczbami całkowitymi!!!")
        with open("zadanie1.txt",'w') as plik:
            plik.write("Wszystkie dane powinny być liczbami całkowitymi!!!")
    else:
        wzor = a**2 + a*b + b**2
        with open("zadanie1.txt",'w') as plik:
            plik.write(str(wzor))
        print(wzor)
zad1()
def zad2(lista1, lista2):
    if len(lista1) != len(lista2):
        return ValueError("Listy nie mają tej samej wartośćci!!!")
    else:
        lista3 = []
        for i in range(len(lista1)):
            lista3.append(lista1[i] + lista2[i])
    return lista3
print(zad2([2, 5, 4, 6, 7],[4, 2, 3, 1, 5]))
def zad3():
    with open("tekst.txt", 'r', encoding= "utf-8") as plik:
        tekst = plik.read()
    znaki = tekst[100:135]
    duze = [litera for litera in znaki if litera.isupper()]
    ilosc_duzych = len(duze)
    if ilosc_duzych > 0:
        print(f"Duże litery we fragmencie to: {duze}. Ich ilość wynisi: {ilosc_duzych}")
    else:
        print("We fragmencie nie ma dużych liter.")
zad3()
def zad4():
    lista = [3, 4, 7, 16, 48, 27]
    a = 5
    liczby = [i for i in lista if i>a]
    print(liczby)
zad4()
def zad5():
    a = pow(pow(math.e, 3) + pow(math.cos(39), 2),1/5) + pow(2/7,3) + math.pi
    print(a)
zad5()