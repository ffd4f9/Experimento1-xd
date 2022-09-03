from Persona import Persona
if __name__ == "__main__":
    personas = []
    personas.append(Persona("Wagner",24,1.75))
    personas.append(Persona("Luis",22,1.75))
    personas.append(Persona("Bryan",29,1.75))
    personas.append(Persona("Dennis",24,1.70))
    personas.append(Persona("Alejandro",22,1.75))
    personas.append(Persona("Monica",21,1.60))
    print("**********")
    for persona in personas:
        persona.mostrar()
        print("**********")
