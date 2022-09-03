class Persona:
    def __init__(self,nombre:str,edad:int,estatura:float):
        self.__nombre = nombre
        self.__edad = edad
        self.__estatura = estatura

    def mostrar(self):
        print(f"nombre: {self.__nombre}\nedad: {self.__edad}\nestatura: {self.__estatura}")