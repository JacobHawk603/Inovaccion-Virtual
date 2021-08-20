import random

#para instalar esto necesitas:
# python -m pip install -u pip
# python -m pip install -u matplotlib
import matplotlib.pyplot as plt

print(random.randint(1,20))

#generar un numero aleatorio
print(random.randrange(10, 100, 2))

#Reacomodar una lista al azar

lista = [1,2,3,4,5,6,7,8,9,10]
print('Lista original', lista)

random.shuffle(lista)
print('Lista mixeada', lista)

campana = [random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()