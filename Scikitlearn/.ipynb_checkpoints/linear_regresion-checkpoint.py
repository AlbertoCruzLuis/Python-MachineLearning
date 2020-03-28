import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

######## IMPORTAR LOS DATOS #########

#Importar los datos de la libreria scikit-learn
boston = datasets.load_boston()
print(boston)

######## ENTENDER LOS DATOS #########

#Verificar informacion del dataset
print(boston.keys())

#Verificar las caracteristicas del dataset
print(boston.DESCR)

#Verificar la cantidad de datos en el dataset
print(boston.data.shape)

#Verificar la informacion de las columnas
print(boston.feature_names)

######## PREPARAR LOS DATOS #########

#Seleccionamos la columna 5 del dataset
X = boston.data[:, np.newaxis, 5]

#Defino los datos correspondientes a las etiquetas
Y = boston.target

#Graficamos los datos 
plt.scatter(X, Y)
plt.xlabel('Numero de habitaciones')
plt.ylabel('Valor Medio')
plt.show()

######### IMPLEMENTACION DE REGRESION LINEAL #########

from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar algoritmos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

#Defino el algoritmo a utilizar
lr = linear_model.LinearRegression()

#Entreno el module_for_loader()
lr.fit(X_train, Y_train)

#Realizo una prediccion
Y_pred = lr.predict(X_test)

#Graficamos los datos junto con el modelo 
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.title('Regresion Lineal Simple')
plt.xlabel('Numero de habitaciones')
plt.ylabel('Valor Medio')
plt.show()

#Mostrar los datos complementarios
print('Datos del modelo Regresion Lineal Simple')
print('Valor de la pendiente o coeficiente "a"')
print(lr.coef_)
print('Valor de la interseccion o coeficiente "b"')
print(lr.intercept_)
print('La ecuacion del modelo es igual a ')
print('y = ', lr.coef_, 'x ', lr.intercept_)

print('Presicion del modelo:')
print(lr.score(X_train, Y_train))