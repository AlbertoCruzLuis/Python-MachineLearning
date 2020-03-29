import numpy as np
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures 
import matplotlib.pyplot as plt

###### IMPORTAR LOS DATOS #######

boston = datasets.load_boston()
print(boston)

###### COMPRENDER LOS DATOS #######

print(boston.keys())
print(boston.DESCR)
print(boston.feature_names)

###### PREPARAR LOS DATOS ######

#Numero de habitaciones columana numero 6
X_p = boston.data[:, np.newaxis, 5]

y_p = boston.target

#Graficamos los datos
plt.scatter(X_p, y_p)
plt.show()

###### IMPLEMENTACION DE REGRESION POLINOMIAL ######

from sklearn.model_selection import train_test_split

#Separar datos en entrenamiento y prueba
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_p, y_p, test_size=0.2)

#Definimos el grado del Polinomio
poli_reg = PolynomialFeatures(degree = 2)

#Transformar la caracteristicas en dependencia del grado del polinomio
X_train_poli = poli_reg.fit_transform(X_train_p)
X_test_poli = poli_reg.fit_transform(X_test_p)

#Definimos el algoritmo a utilizar
pr = linear_model.LinearRegression()

#Entrenamos el modelo
pr.fit(X_train_poli, y_train_p)

#Reailizar una prediccion
Y_pred_pr = pr.predict(X_test_poli)

#Graficamos los datos junto con el modelo
plt.scatter(X_test_p, y_test_p)
plt.plot(X_test_p, Y_pred_pr, color='red', lineWidth=3)
plt.show()

#Datos del modelo de regresion polinomial
print('DATOS DEL MODELO REGRESION POLINOMIAL')

print('Valor de la pendiente o coeficiente "a":')
print(pr.coef_)

print('Valor de la interseccion o coeficiente "b":')
print(pr.intercept_)

#Cuanto mas se acerque a 1 mejor sera el algoritmo
print('Presicion del modelo:')
print(pr.score(X_train_poli, y_train_p))