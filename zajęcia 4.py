def zad1():
    liczby = list(range(31))
    liczby = [x*2 for x in liczby]
    plik = open("zajęcia4.txt", "w")
    for liczba in liczby:
        plik.write(str(liczba) + '\n')
    plik.close()
zad1()
def zad2():
    plik = open('zajęcia4.txt', 'r')
    liczby = plik.read()
    plik.close()
    print(liczby)
    print('\n')
zad2()
def zad3():
    with open('zajęcia4.txt', 'w', encoding = 'utf-8') as plik:
        plik.write("Lubie placki z dżemem malinowym\n")
        plik.write("Lubie placki z dżemem malinowym\n")
        plik.write("Lubie placki z dżemem malinowym\n")
    with open('zajęcia4.txt', 'r', encoding = 'utf-8') as plik:
        czytanie = plik.read()
        print(czytanie)
zad3()
class NaZakupy:
    def __init__(self, nazwa_produktu, ilość, jednosta_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilość = ilość
        self.jednostka_miary = jednosta_miary
        self.cena_jed = cena_jed
    def wyświetl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilość, self.jednostka_miary)
        print(self.cena_jed)
    def ile_produktu(self):
        return f"{self.ilość} {self.jednostka_miary}"
    def ile_kosztuje(self):
        koszt = self.ilość * self.cena_jed
        return f"{koszt} zł"
ziemniaki = NaZakupy("ziemniaki", 3, "kg", 2)
ziemniaki.wyświetl_produkt()
print(ziemniaki.ile_produktu())
print(ziemniaki.ile_kosztuje())
class Ciągi():
    elementy = []
    def __init__(self, a1 = 0, r = 0, n = 10):
        self.a1 = a1
        self.r = r
        self.n = n
    def wyswietl_dane(self):
        print("Elementy ciągu arytmetycznego: ", self.elementy)
    def pobierz_elementy(self):
        ilość_elementów = int(input("Podaj ilość elementów ciągu: "))
        for x in range(ilość_elementów):
            elementy = float(input(f"Podaj wartość {1+x} elementu: "))
            self.elementy.append(elementy)
    def pobierz_parametry(self):
        self.a1 = float(input("Podaj pierwszą wartość ciagu: "))
        self.r = float(input("Podaj różnicę ciagu: "))
        self.n = int(input("Podaj ilość elementów ciagu: "))
        self.elementy = [self.a1 + x * self.r for x in range(self.n)]
    def policz_sume(self):
        suma = sum(self.elementy)
        print("Suma ciągu = ", suma)
    def policz_elementy(self):
        if self.a1 != 0 and self.r != 0:
            print("Liczba elementów ciągu = ", self.n)
ciągi = Ciągi()
ciągi.pobierz_elementy()
ciągi.wyswietl_dane()
ciągi.policz_elementy()
ciągi.pobierz_parametry()
ciągi.wyswietl_dane()
ciągi.policz_sume()
ciągi.policz_elementy()
class Robaczek:
    krok = 2
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y
    def idz_w_gore(self, ile_kroków):
        self.y += ile_kroków * self.krok
    def idz_w_dol(self, ile_kroków):
        self.y -= ile_kroków * self.krok
    def idz_w_prawo(self, ile_kroków):
        self.x += ile_kroków * self.krok
    def idz_w_lewo(self, ile_kroków):
        self.x -= ile_kroków * self.krok
    def pozycja(self):
        print(f"Współżędne x: {self.x}\nWspółżędne y: {self.y}")
robaczek = Robaczek(5, 5)
robaczek.pozycja()
robaczek.idz_w_gore(5)
robaczek.pozycja()
robaczek.idz_w_dol(4)
robaczek.pozycja()
robaczek.idz_w_prawo(10)
robaczek.pozycja()
robaczek.idz_w_lewo(2)
robaczek.pozycja()