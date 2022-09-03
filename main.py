from Persona import Persona,Empleado
if __name__ == "__main__":
    personas = []
    personas.append(Persona("Wagner",24,1.75))
    personas.append(Empleado("Luis",22,1.75,"Profesor",3))
    personas.append(Persona("Bryan",29,1.75))
    personas.append(Empleado("Dennis",24,1.70,"Biologo",1))
    personas.append(Persona("Alejandro",22,1.75))
    personas.append(Empleado("Monica",21,1.60,"Trabajadora Social",2))
    print("**********")
    for persona in personas:
        persona.mostrar()
        print("**********")
    print("FIN")
