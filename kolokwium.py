import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sns.set(rc={'figure.figsize': (8, 8)})
# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16], label='linia nr',
#              color='red', markers='o', linestyle=':')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Wykres liniowy')
# plt.show()

# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# wykres = sns.relplot(kind='line', data=s, label='dane z serii')
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('Wykres liniowy')
# wykres.set_xlabels('indeks')
# wykres.set_ylabels('wartość')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
# plt.show()

# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['yellow', 'green', 'red'])
# plt.xlabel('indeksy')
# plt.title('Wykres liniowy')
# plt.show()

# data={'a':np.arange(10),
#       'c':np.random.randint(0, 50, 10),
#       'd':np.random.randn(10)}
# data['b'] = data['a'] + 10 * np.random.randn(10)
# data['d'] = np.abs(data['d']) * 100
# df = pd.DataFrame(data)
#
# plot = sns.relplot(data=df, x='a', y='b', hue='c',
#                    palette='bright', size = 'd', legend=True)
# plot.set(xticks=data['a'])
# plt.show()
