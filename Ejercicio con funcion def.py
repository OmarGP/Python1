from datetime import datetime

class Alumno:
    #fecha = datetime.now().date()
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    def __init__(self, nombre, apell1, apell2) -> None:
        self.Nombre = nombre
        self.Apellido1 = apell1
        self.Apellido2 = apell2

    def getNombreCompleto(self) -> None:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"

    def setFechaNacimiento(self, fecha):
        try:
            if(fecha == True):
                self.FechaNacimiento =  datetime.strptime(fecha, "%d-%m-%Y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()

            return
        except:
            pass
        

    def getEdad(self) -> int:
        if (self.FechaNacimiento == None): 
            return ValueError
        else:
            return datetime.now().year - self.FechaNacimiento.year
            

alumno = Alumno("Omar", "García", "Prado")
print(f"{alumno.getNombreCompleto()}")
fecha = input("Dime tu fecha de nacimiento: ")
alumno.setFechaNacimiento(fecha)
print(f"Tu naciste el: " + str(fecha))
print(f"Y tienes {alumno.getEdad()} " + "años.")