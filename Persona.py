class Persona:
    def __init__(self,nombre:str,edad:int,estatura:float):
        self.__nombre = nombre
        self.__edad = edad
        self.__estatura = estatura

    def mostrar(self):
        print(f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nEstatura: {self.__estatura}")
class Empleado(Persona):
    def __init__(self,nombre:str,edad:int,estatura:float,especialidad:str,tiempoActivo:int):
        super().__init__(nombre,edad,estatura)
        self.__especialidad = especialidad
        self.__tiempoActivo = tiempoActivo
    def mostrar(self):
        super().mostrar()
        print(f"Especialidad: {self.__especialidad}\nTiempo activo: {self.__tiempoActivo} periodos")
