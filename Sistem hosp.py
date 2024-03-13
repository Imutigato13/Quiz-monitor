import datetime as datetime
from validaciones import *
class Bioinstrumentos:

    def __init__(self, medico, estado, tamaño, material, fecha_revision, fecha_mantenimiento):
        self.__medico = medico
        self.__estado = estado
        self.__tamaño = tamaño
        self.__material = material
        self.__fecha_implantacion = datetime.datetime.now().strftime("%d/%m/%Y")
        self.__fecha_revision = fecha_revision
        self.__fecha_mantenimiento = fecha_mantenimiento

    #Get's definidos 
    def getMedico(self):
        return self.__medico
    def getEstado(self):
        return self.__estado
    def getTamaño(self):
        return self.__tamaño
    def getMaterial(self):
        return self.__material
    def getFecha_implante(self):
        return self.__fecha_implantacion
    def getFecha_revision(self):
        return self.__fecha_revision
    def getFecha_mantenimiento(self):
        return self.__fecha_mantenimiento
    
    #Set's definidos
    def setMedico(self, med):
        self.__medico = med
    def setEstado(self, est):
        self.__estado = est
    def setTamaño(self, tam):
        self.__tamaño = tam
    def setMaterial(self, mat):
        self.__material = mat
    def setFecha_revision(self, fr):
        self.__fecha_revision = fr
    def setFecha_mantenimiento(self, fm):
        self.__fecha_revision = fm

class Protesis_de_cadera(Bioinstrumentos):

    def __init__(self, medico, estado, tamaño, material, tipo_fijacion, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, tamaño, material, fecha_revision, fecha_mantenimiento)
        self.__tipo_fijacion = tipo_fijacion
    
    def getTipo_fijacion(self):
        return self.__tipo_fijacion
    
    def setTipo_fijacion(self, tf):
        self.__tipo_fijacion = tf

class Marcapasos_cardiacos(Bioinstrumentos):

    def __init__(self, medico, estado, n_electrodos, alam_inal, frecuencia_estimulacion, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, fecha_revision, fecha_mantenimiento)
        self.__n_electrodos = n_electrodos
        self.__alam_inal = alam_inal
        self.__frecuencia_estimulacion = frecuencia_estimulacion
    
    def getN_electrodos(self):
        return self.__n_electrodos
    def getAlam_inal(self):
        return self.__alam_inal
    def getFrecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion
    
    def setN_electrodos(self, ne):
        self.__n_electrodos = ne
    def setAlam_inal(self, ai):
        self.__alam_inal = ai
    def setFreciencia_estimulacion(self, fe):
        self.__frecuencia_estimulacion = fe

class Stents_coronarios(Bioinstrumentos):

    def __init__(self, medico, estado, longuitud, diametro, material, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, material, fecha_revision, fecha_mantenimiento)
        self.__longuitud = longuitud
        self.__diametro = diametro
    
    def getLonguitud(self):
        return self.__longuitud
    def getDiametro(self):
        return self.__diametro
    
    def setLonguitud(self,l):
        self.__longuitud = l
    def setDiametro(self,d):
        self.__diametro = d

class Implantes_dentales(Bioinstrumentos):

    def __init__(self, medico, estado, forma, material, sistema_fijacion, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, material, fecha_revision, fecha_mantenimiento)
        self.__forma = forma
        self.__sistema_fijacion = sistema_fijacion

    def getForma(self):
        return self.__forma
    def getSistema_fijacion(self):
        return self.__sistema_fijacion
    
    def setForma(self, f):
        self.__forma = f
    def setSistema_fijacion(self, sf):
        self.__sistema_fijacion = sf

class Protesis_rodilla(Bioinstrumentos):

    def __init__(self, medico, estado, tamaño, material, tipo_fijacion, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, tamaño, material, fecha_revision, fecha_mantenimiento)
        self.__tipo_fijacion = tipo_fijacion
    
    def getTipo_fijacion(self):
        return self.__tipo_fijacion
    
    def setTipo_fijacion(self, tf):
        self.__tipo_fijacion = tf

class Paciente():

    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula

    def getNombre(self):
        return self.__nombre
    def getCedula(self):
      return self.__cedula

    def setNombre(self, n):
      self.__nombre = n
    def setCedula(self, c):
      self.__cedula = c

class Sistema_hospital:

    def __init__(self):
        self.__registro = {}
    
    def getRegistro(self):
        return self.__registro
    
    def existenciaPaciente(self, paciente):
        if paciente in self.__registro:
            return True
        return False
    
    def existenciaBioinstrumento(self, bioinstrumento):
        if bioinstrumento in self.__registro:
            print(f"El bioinstrumento {bioinstrumento} esta registrado")
            return True
        print(f"El bioinstrumento {bioinstrumento} no esta registrado")
        return False

    def registrarPaciente(self, paciente):
        if self.existenciaPaciente(paciente):
            print(f"El paciente {paciente.getNombre()} esta registrado")
        else:
            self.__registro[paciente] = ()

    def registrarBioinstrumento(self, paciente, bioinstrumento):
        if self.existenciaPaciente(paciente):
            self.__registro[paciente].append(bioinstrumento)
        else:
            print(f"El paciente {paciente.getNombre()} no esta registrado")

    def retirarBioinstrumento(self, paciente, bioinstrumento):
        if self.existenciaPaciente(paciente):
            self.__registro[paciente].remove(bioinstrumento)
        else:
            print(f"El paciente {paciente.getNombre()} no esta registrado")

def main():

    sh = Sistema_hospital()
    print("Bienvenido al sistema hospitalario de gestion de bioisntrumentos".center(90))
    while True:

        print("Menu principal".center(90))
        men1 = validar_entero("""\r1.Registrar paciente
                                \r2.Modificar registro de un paciente
                                \r3.Revisar estado de bioinstrumento
                                \r4.Finalizar programa
                                \r:""")
        
        if men1 == 1:

            print("Registro de pacientes".center(90))
            nombre = validar_alfanumerico("Ingrese el nombre el paciente: ").lower()
            cedula = validar_entero("Ingrese el numero de cedula del paciente: ")
            paciente = Paciente(nombre,cedula)
            sh.registrarPaciente(paciente)
            print(f"El paciente {paciente.getNombre()} se registro con exito")
        
        elif men1 == 2:

            nombre = validar_alfanumerico("Ingrese el nombre el paciente: ").lower()
            cedula = validar_entero("Ingrese el numero de cedula del paciente: ")
            registro = sh.getRegistro()

            for paciente in registro.keys():
                if paciente.getNombre() == nombre and paciente.getCedula() == cedula:
                    print(f"Que decea modificar de {paciente.getNombre()}?".center(90))

                    men2 = validar_entero("""\r1.Registrar bioinstrumento
                                            \r2.Retirar bioinstrumento
                                            \r3.Modificar bioinstrumento
                                            \r4.Registro completo de bioinstrumentos
                                            \r5.Salir
                                            \r:""")
                    
                    if men2 == 1:

                        men3 = validar_entero(""" """)
        
        elif men1 == 4:

            print("Vuelva pronto")
            break
