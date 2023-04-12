import math
def zad1():
    with open("tekst.txt", 'r', encoding = 'utf-8') as plik:
        tekst = plik.read()
    znaki = tekst[71:111]
    litery = [i for i in znaki if i == "A"]
    ile = len(litery)
    print(znaki)
    if ile == 0:
        print("Nie ma liter A w tekście!!!")
    else:
        print(f"W tekście liter A jest: {ile}")
#zad1()
def zad2():
    lista = [1, 4.5, 3, 5.6]
    lista2 = [i for i in lista if isinstance(i, float)]
    print(lista)
    print(lista2)
#zad2()
def zad3(lista):
    for i in range(1, len(lista)):
        temp = lista[i]+lista[0]
        lista.append(temp)
    return lista
#print(zad3([1,5, 4.5 , 9, 2, 4.56]))
def zad4():
    wynik = pow(math.sin(56),2) + pow((4**2)/25 + math.log(85,3),1/4)
    print(round(wynik, 2))
#zad4()
def zad5():
    try:
        n = int(input("Podaj liczbę n: "))
    except ValueError:
        print("Dane powinny być liczbami całkowitymi!!!")
        with open("zadanie5.txt","w+") as plik:
            plik.write("Dane powinny być liczbami całkowitymi!!!")
    else:
        suma=0
        for i in range(n):
            suma+=i
    print(suma+n)
    with open("zadanie5.txt","w") as plik:
        plik.write(str(suma+n))
#zad5()
