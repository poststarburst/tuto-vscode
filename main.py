"""

print("Hola Mundo!! Me llamo Marlon E...!")
print("Hola Mundo!! 1...!")
print("Hola Mundo!! 2...!")
print("Hola Mundo!! 3...!")
#Soy un comentario
print("Hola Mundo!! Me llamo Marlon E...!")


Texto que no se va a interpretar
Texto que no se va a interpretar
Texto que no se va a interpretar
Texto que no se va a interpretar

"""

# Variables
texto = "Repaso de Python con Victor"
nombre = "Marlon Garza"
altura = "185 cm"
year = 2023

"""

#print(texto)

#print(f"{texto} - {nombre} - {altura} - {str(year)}")
#print(texto + " - " + nombre + " - " + altura + " - " + str(year))

#Entrada
#sitioweb = input("¿Cuál es tu página web?: ")
#print("El sitio web del usuario es: " + sitioweb)

"""

# Condiciones

"""

altura = int(input("¿Cuál es tu altura?: "))
if altura >= 180:
     print("Eres una persona alta!!")
else: 
    print("eres CHAPARRO!!")    

"""
"""
#Funciones

var_altura = int(input("¿Cuál es tu altura?: "))

def mostrarAltura(altura):
     resultado = ""

     if altura >= 180:
          resultado = "Eres una persona alta!!"
     else: 
          resultado = "Eres CHAPARRO!!"
     
     return resultado

print(mostrarAltura(var_altura))

"""


#Listas
personas = ["Victor", "Pedro", "Juan", "Ramon", "Santiago"]
print(personas[0])

for persona in personas:
    print("-" + persona)
















