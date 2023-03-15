import math
# zadanie 1
print(math.e**10)
print(pow(math.log(5+pow(math.sin(8),2)),1/6))
print(round(3,55))
print(math.ceil(4.80))
# zadanie 2
imie = "MICHAŁ"
nazwisko = "KORNATOWSKI"
print(imie.capitalize(), nazwisko.capitalize())
# zadanie 3
piosenka = " pubie placki la la la la z dżemem"
print(piosenka.count(" la"))
# zadanie 4
print(imie[1])
print(imie[len(imie)-1])
# zadanie 5
łańcuch = "Żakś bardzo lubi Bambi IRL i słucha tego 2.5 razy na 1 dzień"
print(łańcuch.split())
# zadanie 6
tekst = "coś"
dziesiętne = 2.55
szesnastkowe = 0xAD5
print(tekst, dziesiętne, "{0:X}".format(szesnastkowe))
# zadanie 7
lista = ["piłka nożna", "siatkówka", "piłka ręczna", "hokej"]
print(lista[::-1])
lista.insert(len(lista), "bieganie")
lista.insert(len(lista), "pływanie")
lista.insert(len(lista),"tenis")
print(lista)
# zadanie 8
słownik = {"pt":"pod tytułem", "itd":"I tak dalej", "itp":"I temu podobne"}
print(słownik)
# zadanie 9
gry = {1:"Wieźmin 3", 2:"GOW", 3:"TLOU", 4:"Skyrim"}
print(len(gry))
# zadanie 10
zdanie = input("Podaj zdanie: ")
print(zdanie.count("a"))
# zadanie 11
a = 5
b = 4
c = 2
if a>b and a>c:
    print("Największe jest: ", a)
elif b>a and b>c:
    print("Największe jest: ", b)
else:
    print("Największe jest: ", c)
# zadanie 12
liczby = [2, 3.56, 5, 16, 5.5]
for x in range(len(liczby)):
    print(liczby[x]**2)
# zadanie 13
parzyste = []
while len(parzyste) < 10:
    k=int(input("Podaj liczby: "))
    if k%2==0:
        parzyste.append(k)
