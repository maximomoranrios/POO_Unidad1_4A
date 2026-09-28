"""
Ejercicio Práctico #2: “Modelar y Diagramar en POO”
"""

print("\033c")


# Clase Coches
class Coches:
    def __init__(self, color, marca, velocidad):
        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad

    def acelerar(self):
        self.__velocidad+= 1
        return self.__velocidad

    def frenar(self):
        self.__velocidad-= 1
        return self.__velocidad

    def tocar_claxon(self):
        return "pi pi pi"


# Crear objetos de la clase Coches
coche1 = Coches("Blanco", "VW", 220)
coche2 = Coches("Azul", "Nissan", 180)

print(f"El coche aumenta la velocidad a: {coche1.acelerar()}")
print(f"El coche aumenta la velocidad a: {coche1.acelerar()}")
print(f"El coche aumenta la velocidad a: {coche1.acelerar()}")
print(f"El coche reduce la velocidad a: {coche1.frenar()}")
print(f"El coche toca el claxon: {coche1.tocar_claxon()}")





