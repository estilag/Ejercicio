# Módulo Modelo
# Contiene la clase Cliente


# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre=" ", dir=" ", tlf=0, email=" ", factanual=0):
        self.nombre = nombre
        self.dir = dir
        self.tlf = tlf
        self.email = email
        self.factanual = factanual

    def getNombre(self):
         return self.nombre
    def setNombre(self, nombre):
         self.nombre = nombre

    def getDir(self):
        return self.dir
    def setDir(self, dir):
        self.dir = dir

    def getTlf(self):
        return self.tlf
    def setTlf(self, tlf):
        self.tlf = tlf

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email

    def getFactanual(self):
        return self.factanual
    def setFactanual(self, factanual):
        self.factanual = factanual

    # Función que devuelve el Listado con todos los datos
    def __str__(self):
        listado = "Cliente[nombre:"+ self.nombre+ ", dir:"+ self.dir+ ", tlf:"+ str(self.tlf)+", email:"+ self.email+ ", factanual:"+ str(self.factanual)+"]"
        return listado

# Creo cuatro clientes

