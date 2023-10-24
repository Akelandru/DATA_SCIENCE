import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
colors = []

setosa = sns.load_dataset("iris")
versicolor = sns.load_dataset("iris")
virginica = sns.load_dataset("iris")

for i in df.index:
    if df.loc[i, "species"] == "setosa":
        versicolor.drop(i, inplace = True)
        virginica.drop(i, inplace = True)
        colors.append('blue')
    elif df.loc[i, "species"] == "versicolor":
        setosa.drop(i, inplace = True)
        virginica.drop(i, inplace = True)
        colors.append('green')
    else:
        setosa.drop(i, inplace = True)
        versicolor.drop(i, inplace = True)
        colors.append('red')

setosa.drop(columns = "species", inplace = True)
virginica.drop(columns = "species", inplace = True)
versicolor.drop(columns = "species", inplace = True)

print(setosa.std())
print(virginica.std())
print(versicolor.std())

df.plot(kind = 'scatter', x='sepal_length', y='petal_length', c = colors)
plt.show()

