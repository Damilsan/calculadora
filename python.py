# Crear un programa que pida al usuario su nombre y lo salude.
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "! Bienvenido/a.")

# Crear un programa que pida al usuario su edad y determine si es mayor de edad o no.
edad = int(input("¿Cuántos años tienes?"))

if edad >= 18:
    print ("Binevenido, puedes ingresar")
    
else:
    print ("Lo siento, no puedes ingresar")
    
# Crear un programa que pida al usuario un número y determine si es par o impar.
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Crear un programa que pida al usuario una palabra y determine si es un palíndromo.   
palabra = input("Introduce una palabra: ")
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")  
else:
    print("La palabra no es un palíndromo.")
    
# declarar variables
nombre = "Juan"
edad = 25
ciudad = "Santa Marta"

# Imprimir variables    
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ")    
print("Los datos ingresados son:")
print("Nombre:", nombre)
print("Edad:", edad)   
print("Ciudad:", ciudad)

# Crear un programa que pida al usuario dos números y muestre su suma, resta, multiplicación y división.
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2 
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)


# crear una lista y un bucle for para imprimir los elementos de la lista
lista = ["manzana", "banana", "naranja", "uva"]
for fruta in lista:
    print(fruta)

# crear un diccionario y un bucle for para imprimir las claves y valores del diccionario
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Santa Marta"}  
for clave, valor in diccionario.items():
    print(clave + ":", valor)