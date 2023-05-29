import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# y = np.arange(4)
# plt.plot(y)
# plt.ylabel('liczby')
# plt.show()

# x = np.array([1,2,3,4])
# y = x**2
# plt.plot(x, y, 'ro-')
# plt.axis([0,6, 0,20])
# plt.show()
#
# plt.plot(x, y, 'r')
# plt.plot(x, y, 'o')
# plt.axis([0,6, 0,20])
# plt.show()

# a = np.arange(0, 5, 0.2)
# plt.plot(a, a, 'r--', a, a**2, 'bs', a, a**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'], loc='center left')
# plt.show()

# z = np.arange(0, 5, 0.2)
# plt.plot(z, z, 'r--', label='liniowa')
# plt.plot(z, z**2, 'bs', label='kwadratowa')
# plt.plot(z, z**3, 'g^', label='sześcienna')
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# plt.title('Wykres liniowy')
# plt.legend()
# plt.savefig('wykres1.png')
# plt.show()

# x = np.arange(0, 10.1, 0.1)
# y = np.sin(x)
# plt.plot(x, y, 'b-')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Sinus')
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.rand(50)}
# data['b'] = data['a'] + 10 * np.random.rand(50)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# plt.xlabel('wartości a')
# plt.ylabel('wartości b')
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2* np.pi *x1)
# y2 = np.cos(2* np.pi *x2)
#
# plt.subplot(4, 1, 1)
# plt.plot(x1, y1)
# plt.title('Wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(4, 1, 4)
# plt.plot(x2, y2, 'r')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('Wykres cos(x)')
#
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1, 'g-')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('Wykres sin(x)')
#
# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[1, 1].set_title('Wykres cos(x)')
#
# axs[2, 0].plot(x1, y1, 'y-')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('sin(x)')
# axs[2, 0].set_title('Wykres sin(x)')
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
#
# plt.show()
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azia', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [12111111, 212321323, 32132423, 321323]}
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosc = list(grupa.agg('Populacja').sum())
#
# plt.bar(etykiety, wartosc, color=['yellow', 'red', 'green'])
# plt.xlabel('Kontynent')
# plt.ylabel('Populacja w mld')
# plt.show()
#
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# ts.plot()
# plt.show()

# #korzystając z funkcji random oraz data_rangemożemy wygenerować szereg czasowy danych
# ts = pd.Series(np.random.randn(1000))
# # #funkcja biblioteki pandas generująca skumulowaną sumę kolejnych elementów
# ts = ts.cumsum()#rzutowanie Series na DataFrame
# df = pd.DataFrame(ts, columns=['wartości'])
# print(df)
# # dodanie nowej kolumny i wykorzystanie funkcji rolling do stworzenia kolejnych wartości średniej kroczącej
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

# x = np.random.randn(10000)
# plt.hist(x, bins=59, facecolor='g', alpha=0.75, density=True)
# plt.xlabel('Wartość')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()

df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
print(df)
seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges, texts, autotext = plt.pie(x = seria, labels=seria.index,
                                  autopct=lambda pct: "{:.1f}%".format(pct),
                                  textprops=dict(color="black"),
                                  colors=['red', 'green'])
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc = 'lower right')
plt.ylabel('Procentowy wynik wartości zamówień')
plt.show()
