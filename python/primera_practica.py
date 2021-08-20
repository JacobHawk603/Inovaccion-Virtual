#Esto es un comentario en python


#cadena de caracteres
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}")
print("hola, {}!".format(nombre)) #otra forma de imprimir la linea anterior, puedes precindir de esta linea

#entero

edad = 25

#flotante - decimales
altura = 1.75

#convertir flotante
edadString= str(edad)

print(edad + edad)
print(edadString+edadString)

print(type(edad))

tuEdad = input("introduce tu edad: ")
tuEdad=int(tuEdad)

#condicionales if

if tuEdad >= 18 and tuEdad < 100:
    print("Eres mayor de edad")
elif tuEdad>100:
    print("eres inmortal")
elif tuEdad <= 0:
    print("no existes")
else:
    print("Eres menor de edad")

#Ciclo for

for i in range(0, 10):
    print(i)

