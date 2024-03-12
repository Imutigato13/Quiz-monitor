import datetime as datetime

class Bioinstrumentos:

    def __init__(self, medico, estado, tamaño, material):
        self.__medico = medico
        self.__estado = estado
        self.__tamaño = tamaño
        self.__material = material
        self.__fecha = datetime.datetime.now().strftime("%d/%m/%Y")
    
    #Get's definidos 
    def getMedico(self):
        return self.__medico
    def getEstado(self):
        return self.__estado
    def getTamaño(self):
        return self.__tamaño
    def getMaterial(self):
        return self.__material
    def getFecha(self):
        return self.__fecha
    
    #Set's definidos
    def setMedico(self, med):
        self.__medico = med
    def setEstado(self, est):
        self.__estado = est
    def setTamaño(self, tam):
        self.__tamaño = tam
    def setMaterial(self, mat):
        self.__material = mat

class Protesis_de_cadera(Bioinstrumentos):

    def __init__(self, medico, estado, tamaño, material, tipo_fijacion):
        super().__init__(medico, estado, tamaño, material)
        self.__tipo_fijacion = tipo_fijacion
    
    def getTipo_fijacion(self):
        return self.__tipo_fijacion
    
    def setTipo_fijacion(self, tf):
        self.__tipo_fijacion = tf

class Marcapasos_cardiacos(Bioinstrumentos):

    def __init__(self, medico, estado, n_electrodos, alam_inal, frecuencia_estimulacion):
        super().__init__(medico, estado)
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

    def __init__(self, medico, estado, longuitud, diametro, material):
        super().__init__(medico, estado, material)
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

    def __init__(self, medico, estado, forma, material, sistema_fijacion):
        super().__init__(medico, estado, material)
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

    def __init__(self, medico, estado, tamaño, material, tipo_fijacion):
        super().__init__(medico, estado, tamaño, material)
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
        print(f"El paciente {paciente.getNombre()} no esta registrado")
        return False
    
    def existenciaBioinstrumento(self, bioinstrumento):
        if bioinstrumento in self.__registro:
            print(f"El bioinstrumento {bioinstrumento} esta registrado")
            return True
        print(f"El bioinstrumento {bioinstrumento} no esta registrado")
        return False

    def agregarPaciente(self, paciente):
        if self.existenciaPaciente(paciente):
            print(f"El paciente {paciente.getNombre()} esta registrado")
        else:
            self.__registro[paciente] = ()

    def agregarBioinstrumento(self, paciente, bioinstrumento):
        if self.existenciaPaciente(paciente):
            

