# -*- coding: utf-8 -*-
"""Copia de CaliforniaHousing_EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SD7MTmh-3GbOUxHjTylc4NN26dbUnCxM
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

california_train = pd.read_csv("/content/sample_data/california_housing_train.csv")
california_test = pd.read_csv("/content/sample_data/california_housing_test.csv")

california_all =  pd.concat([california_train, california_test], ignore_index=True)

california_all.head(10)



california_all.info()

california_all.shape

california_all.describe

california_all['housing_median_age'].hist(bins=30)

plt.figure(figsize=(15,17))
sns.boxplot(x="population",y="housing_median_age", data=california_all)
plt.show()

from scipy.stats import skewtest, levene

#Temas de ciencias blandas --> Rechazar < 0.01

print(skewtest(california_all["longitude"]))
print(skewtest(california_all["latitude"]))
print(skewtest(california_all["population"]))
print(skewtest(california_all["households"]))
print(skewtest(california_all["total_rooms"]))

sns.histplot(data = california_all, x = "housing_median_age", kde = True, bins=20)

sns.histplot(data = california_all, x = "households", kde = True, bins=20)



"""Observamos que sí hay una relación lineal entre las variables. Sin embargo, los tests de uniformidad de la distribución y homogeneidad arrojan resultados negativos. Por lo tanto, la prueba de correlación apropiada para usar sería una prueba no paramétrica como la correlación de Spearman o de Kendall.

"""

corr_s = california_all.corr(method = "spearman")

corr_s["housing_median_age"].sort_values(ascending=False)

corr_s["population"].sort_values(ascending=False)

sns.heatmap(corr_s)

