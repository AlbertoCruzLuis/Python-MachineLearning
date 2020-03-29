import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#Cargamos los datos
data = load_iris()

#Entender los datos
print(data)
print(data.keys())
print(data.target_names)
print(data.DESCR)
print(data["data"][0])

#Preparar los datos
X = data.data[:,np.newaxis,0]
Y = data.target
X1 = data.data[:, np.newaxis,1]

#Graficamos los datos en 2D
fig = plt.figure(figsize=(10,6))
#plt.title("Grafico de Load_iris")
#Mapa de Calor
#sns.heatmap(data.data[:40], annot=True)
#plt.scatter(X,Y)
#Graficar los datos en 3D 
ax = Axes3D(fig, elev=-150, azim=110)
ax.set_title("Grafico 3D")
ax.scatter(X1,Y)
plt.show()
