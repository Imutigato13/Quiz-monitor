import datetime as datetime
from validaciones import *
import random
class Bioinstrumentos:

    def __init__(self, medico, estado, tamaño, material, fecha_revision, fecha_mantenimiento):
        self.__medico = medico
        self.__estado = estado
        self.__tamaño = tamaño
        self.__material = material
        self.__fecha_implantacion = datetime.datetime.now().strftime("%d/%m/%Y")
        self.__fecha_revision = fecha_revision
        self.__fecha_mantenimiento = fecha_mantenimiento
        self.__n_registro = random.randint(1,10000)

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
    def getN_registro(self):
        return self.__n_registro
    
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
        self.__tipo_bioinstrumento = "protesis_cadera"
    
    def getTipo_fijacion(self):
        return self.__tipo_fijacion
    def getTipo_bioinstrumento(self):
        return self.__tipo_bioinstrumento
    
    def setTipo_fijacion(self, tf):
        self.__tipo_fijacion = tf

class Marcapasos_cardiacos(Bioinstrumentos):

    def __init__(self, medico, estado, n_electrodos, alam_inal, frecuencia_estimulacion, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, None, None, fecha_revision, fecha_mantenimiento)
        self.__n_electrodos = n_electrodos
        self.__alam_inal = alam_inal
        self.__frecuencia_estimulacion = frecuencia_estimulacion
        self.__tipo_bioinstrumento = "marcapasos_cardiaco"
    
    def getN_electrodos(self):
        return self.__n_electrodos
    def getAlam_inal(self):
        return self.__alam_inal
    def getFrecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion
    def getTipo_bioinstrumento(self):
        return self.__tipo_bioinstrumento
    
    def setN_electrodos(self, ne):
        self.__n_electrodos = ne
    def setAlam_inal(self, ai):
        self.__alam_inal = ai
    def setFrecuencia_estimulacion(self, fe):
        self.__frecuencia_estimulacion = fe

class Stents_coronarios(Bioinstrumentos):

    def __init__(self, medico, estado, longitud, diametro, material, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, None, material, fecha_revision, fecha_mantenimiento)
        self.__longitud = longitud
        self.__diametro = diametro
        self.__tipo_bioinstrumento = "stents_coronarios"
    
    def getLongitud(self):
        return self.__longitud
    def getDiametro(self):
        return self.__diametro
    def getTipo_bioinstrumento(self):
        return self.__tipo_bioinstrumento
    
    def setLongitud(self,l):
        self.__longitud = l
    def setDiametro(self,d):
        self.__diametro = d

class Implantes_dentales(Bioinstrumentos):

    def __init__(self, medico, estado, forma, material, sistema_fijacion, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, None,material, fecha_revision, fecha_mantenimiento)
        self.__forma = forma
        self.__sistema_fijacion = sistema_fijacion
        self.__tipo_bioinstrumento = "implantes_dentales"
        
    def getForma(self):
        return self.__forma
    def getSistema_fijacion(self):
        return self.__sistema_fijacion
    def getTipo_bioinstrumento(self):
        return self.__tipo_bioinstrumento
    
    def setForma(self, f):
        self.__forma = f
    def setSistema_fijacion(self, sf):
        self.__sistema_fijacion = sf

class Protesis_rodilla(Bioinstrumentos):

    def __init__(self, medico, estado, tamaño, material, tipo_fijacion, fecha_revision, fecha_mantenimiento):
        super().__init__(medico, estado, tamaño, material, fecha_revision, fecha_mantenimiento)
        self.__tipo_fijacion = tipo_fijacion
        self.__tipo_bioinstrumento = "protesis_rodilla"
    
    def getTipo_fijacion(self):
        return self.__tipo_fijacion
    def getTipo_bioinstrumento(self):
        return self.__tipo_bioinstrumento
    
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
    

    def registrarPaciente(self, paciente):
        if self.existenciaPaciente(paciente):
            print(f"El paciente {paciente.getNombre()} está registrado")
        else:
            self.__registro[paciente] = []

    def registrarBioinstrumento(self, paciente, bioinstrumento):
        if self.existenciaPaciente(paciente):
            self.__registro[paciente].append(bioinstrumento)
        else:
            print(f"El paciente {paciente.getNombre()} no está registrado")

    def retirarBioinstrumento(self, paciente, bioinstrumento):
        if self.existenciaPaciente(paciente):
            self.__registro[paciente].remove(bioinstrumento)
        else:
            print(f"El paciente {paciente.getNombre()} no está registrado")

def main():

    sh = Sistema_hospital()
    print("Bienvenido al sistema hospitalario de gestion de bioinstrumentos".center(90))
    while True:

        print("--Menu principal--".center(90))
        menu = validar_entero("""\r1.Registrar paciente
                                 \r2.Modificar registro de un paciente
                                 \r3.Revisar estado de bioinstrumento
                                 \r4.Finalizar programa
                                 \r:""")
        
        if menu == 1:

            print("--Registro de pacientes--".center(90))
            nombre = validar_alfanumerico("Ingrese el nombre del paciente: ").lower()
            cedula = validar_entero("Ingrese el número de cedula del paciente: ")
            paciente = Paciente(nombre,cedula)
            sh.registrarPaciente(paciente)
            print(f"El paciente {paciente.getNombre()} se registró con exito")
        
        elif menu == 2:

            nombre = validar_alfanumerico("Ingrese el nombre del paciente: ").lower()
            cedula = validar_entero("Ingrese el número de cedula del paciente: ")
            registro = sh.getRegistro()

            for paciente in registro.keys():
                if paciente.getNombre() == nombre and paciente.getCedula() == cedula:
                    print(f"--¿Que desea modificar de {paciente.getNombre()}?--".center(90))

                    vbio = validar_entero("""\r1.Registrar bioinstrumento
                                             \r2.Retirar bioinstrumento
                                             \r3.Modificar bioinstrumento
                                             \r4.Registro completo de bioinstrumentos
                                             \r5.Salir
                                             \r:""")
                    
                    if vbio == 1:

                        print("--Seleccione el bioinstrumento a registrar--".center(90))
                        rbio = validar_entero("""\r1.Protesis de cadera
                                                 \r2.Marcapasos cardiaco
                                                 \r3.Stents coronario
                                                 \r4.Implante dental
                                                 \r5.Protesis de rodilla
                                                 \r: """)
                        
                        if rbio == 1:
                            
                            medico = validar_alfanumerico("Ingrese el médico que implantó el bioinstrumento: ")
                            condiciones = validar_alfanumerico("Ingrese el estado del bioinstrumento: ")
                            tamaño = validar_entero("Indique el tamaño del dispositivo en cm: ")
                            material = validar_alfabetico("Ingrese el material del bioinstrumento: ")
                            tipo_fijacion = validar_alfanumerico("¿Cuál es el tipo de fijación que tiene?: ")
                            fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                            fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')

                            protesis_cadera = Protesis_de_cadera(medico,condiciones,tamaño,material,tipo_fijacion,fecha_revision,fecha_mantenimiento)
                            sh.registrarBioinstrumento(paciente, protesis_cadera)
                            print(f"El bioinstrumento con número de registro {protesis_cadera.getN_registro()} se registró correctamente")
                            break

                        elif rbio == 2:

                            medico = validar_alfanumerico("Ingrese el médico que implant el bioinstrumento: ")
                            condiciones = validar_alfanumerico("Ingrese el estado del bioinstrumento: ")
                            n_electrodos = validar_entero("Ingrese la cantidad de electrodos que se tiene: ")
                            alam_inal = validar_alfanumerico("Ingrese si el marcapasos es alambrico o inalambrico: ")
                            frecuencia_estimulacion = validar_entero("Ingrese el tiempo de estimulación en segundos: ")
                            fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                            fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')

                            marcapasos = Marcapasos_cardiacos(medico,condiciones,n_electrodos,alam_inal,frecuencia_estimulacion,fecha_revision,fecha_mantenimiento)
                            sh.registrarBioinstrumento(paciente, marcapasos)
                            print(f"El bioinstrumento con número de registro {marcapasos.getN_registro()} se registró correctamente")
                            break
                            
                        elif rbio == 3:

                            medico = validar_alfanumerico("Ingrese el médico que implantó el bioinstrumento: ")
                            condiciones = validar_alfanumerico("Ingrese el estado del bioinstrumento: ")
                            longitud = validar_entero("Introduzca la longitud del bioisntrumento en cm: ")
                            diametro = validar_entero("Introduzca el diametro del bioinstrumento en cm: ")
                            material = validar_alfabetico("Ingrese el material del bioinstrumento: ")
                            fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                            fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')

                            stent_coronario = Stents_coronarios(medico,condiciones,longitud,diametro,material,fecha_revision,fecha_mantenimiento)
                            sh.registrarBioinstrumento(paciente,stent_coronario)
                            print(f"El bioinstrumento con número de registro {stent_coronario.getN_registro()} se registró correctamente")
                            break

                        elif rbio == 4:
                            
                            medico = validar_alfanumerico("Ingrese el médico que implantó el bioinstrumento:  ")
                            condiciones = validar_alfanumerico("Ingrese el estado del bioinstrumento:  ")
                            forma = validar_alfabetico("Ingrese el tipo de forma del bioinstrumeno:  ")
                            material = validar_alfabetico("Ingrese el material del bioinstrumento:  ")
                            sistema_fijacion = validar_alfabetico("Ingrese el sistema de fijación del bioinstrumento:  ")
                            fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                            fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')

                            implante_dental = Implantes_dentales(medico,condiciones,forma,material,sistema_fijacion,fecha_revision,fecha_mantenimiento)
                            sh.registrarBioinstrumento(paciente,implante_dental)
                            print(f"El bioinstrumento con número de registro {implante_dental.getN_registro()} se registró correctamente")
                            break

                        elif rbio == 5:

                            medico = validar_alfanumerico("Ingrese el médico que implantó el bioinstrumento: ")
                            condiciones = validar_alfanumerico("Ingrese el estado del bioinstrumento: ")
                            tamaño = validar_entero("Indique el tamaño del dispositivo en cm: ")
                            material = validar_alfabetico("Ingrese el material del bioinstrumento: ")
                            fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                            fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')

                            protesis_rodilla = Protesis_rodilla(medico,condiciones,tamaño,material,fecha_revision,fecha_mantenimiento)
                            sh.registrarBioinstrumento(paciente,protesis_rodilla)
                            print(f"El bioinstrumento con número de registro {protesis_rodilla.getN_registro()} se registró correctamente")
                            break

                    elif vbio == 2:
                        print("--Eliminar bioinstrumento--".center(90))
                        n_registro = validar_entero("Ingrese el número de registro del bioinstrumento: ")
                        for bioinstrumento in registro[paciente]:
                            if n_registro == bioinstrumento.getN_registro():
                                sh.retirarBioinstrumento(paciente, bioinstrumento)
                                print("El bioinstrumento se retiró con exito")
                                break
                        break
                              
                    elif vbio == 3:
                        print("--Modificar bioinstrumento--")
                        n_registro = validar_entero("Ingrese el número de registro del bioinstrumento: ")
                        for bioinstrumento in registro[paciente]:
                            if n_registro == bioinstrumento.getN_registro():
                                
                                if bioinstrumento.getTipo_bioinstrumento() == "protesis_cadera":
                                    mod = validar_entero("""--Modificación--
                                                        \r1. Estado
                                                        \r2. Tamaño
                                                        \r3. Material
                                                        \r4. Tipo de Fijación
                                                        \r5. Fecha de mantenimiento 
                                                        \r:   """)
                                    fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                                    bioinstrumento.setFecha_revision(fecha_revision)
                                    if mod == 1:
                                        nuevo_estado = validar_alfanumerico("Introduzca el nuevo estado del marcapasos cardiaco:  ")
                                        bioinstrumento.setEstado(nuevo_estado)
                                    elif mod == 2:
                                        nuevo_tamaño = validar_alfanumerico("Introduzca el nuevo tamaño:  ")
                                        bioinstrumento.setTamaño(nuevo_tamaño)
                                    elif mod == 3:
                                        nuevo_material = validar_alfanumerico("Introduzca el nuevo material:  ")
                                        bioinstrumento.setMaterial(nuevo_material)
                                    elif mod == 4:
                                        nuevo_tipo_fijacion = validar_alfanumerico("Introduzca el nuevo tipo de fijación:  ")
                                        bioinstrumento.setTipo_fijacion(nuevo_tipo_fijacion)
                                    elif mod == 5:
                                        nueva_fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la nueva fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')
                                        bioinstrumento.setFecha_mantenimiento(nueva_fecha_mantenimiento)
    
                                elif bioinstrumento.getTipo_bioinstrumento() == "marcapasos_cardiaco":
                                    mod = validar_entero("""--Modificación--
                                                        \r1. Estado
                                                        \r2. # Electrodos
                                                        \r3. Alambrico/Inalambrico
                                                        \r4. Frecuencia de estimulación
                                                        \r5. Fecha de mantenimiento 
                                                        \r:   """)
                                    fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                                    bioinstrumento.setFecha_revision(fecha_revision)
                                    if mod == 1:
                                        nuevo_estado = validar_alfanumerico("Introduzca el nuevo estado del marcapasos cardiaco:  ")
                                        bioinstrumento.setEstado(nuevo_estado)
                                    elif mod == 2:
                                        nuevo_N_electrodos = validar_entero("Introduzca el número numero de electrodos:  ")
                                        bioinstrumento.setN_electrodos(nuevo_N_electrodos)
                                    elif mod == 3:
                                        nuevo_alam_inal = validar_alfanumerico("Introduzca si es Alambrico o Inalambrico:  ")
                                        bioinstrumento.setAlam_inal(nuevo_alam_inal)
                                    elif mod == 4:
                                        nuevo_frecuencia_estimulación = validar_entero("Introduzca el nuevo tiempo de estimulación en segundos:  ")
                                        bioinstrumento.setFrecuencia_estimulacion(nuevo_frecuencia_estimulación)
                                    elif mod == 5:
                                        nueva_fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la nueva fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')
                                        bioinstrumento.setFecha_mantenimiento(nueva_fecha_mantenimiento)            
                            
                                elif bioinstrumento.getTipo_bioinstrumento() == "stents_coronarios":
                                    mod = validar_entero("""--Modificación--
                                                        \r1. Estado
                                                        \r2. Longitud
                                                        \r3. Diametro
                                                        \r4. Material
                                                        \r5. Fecha de mantenimiento 
                                                        \r:   """)
                                    fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                                    bioinstrumento.setFecha_revision(fecha_revision)
                                    if mod == 1:
                                        nuevo_estado = validar_alfanumerico("Introduzca el nuevo estado del marcapasos cardiaco:  ")
                                        bioinstrumento.setEstado(nuevo_estado)
                                    elif mod == 2:
                                        nueva_longitud = validar_entero("Introduzca la nueva longitud:  ")
                                        bioinstrumento.setLongitud(nueva_longitud)
                                    elif mod == 3:
                                        nuevo_diametro = validar_entero("Introduzca el nuevo diametro:  ")
                                        bioinstrumento.setDiametro(nuevo_diametro)
                                    elif mod == 4:
                                        nuevo_material = validar_alfanumerico("Introduzca el nuevo material:  ")
                                        bioinstrumento.setMaterial(nuevo_material)
                                    elif mod == 5:
                                        nueva_fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la nueva fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')
                                        bioinstrumento.setFecha_mantenimiento(nueva_fecha_mantenimiento)
                                    
                                elif bioinstrumento.getTipo_bioinstrumento() == "implantes_dentales":
                                    mod = validar_entero("""--Modificación--
                                                        \r1. Estado
                                                        \r2. Forma
                                                        \r3. Material
                                                        \r4. Sistema de Fijación
                                                        \r5. Fecha de mantenimiento 
                                                        \r:   """)
                                    fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                                    bioinstrumento.setFecha_revision(fecha_revision)
                                    if mod == 1:
                                        nuevo_estado = validar_alfanumerico("Introduzca el nuevo estado del marcapasos cardiaco:  ")
                                        bioinstrumento.setEstado(nuevo_estado)
                                    elif mod == 2:
                                        nueva_forma = validar_alfanumerico("Introduzca la nueva forma:  ")
                                        bioinstrumento.setForma(nueva_forma)
                                    elif mod == 3:
                                        nuevo_material = validar_alfanumerico("Introduzca el nuevo material:  ")
                                        bioinstrumento.setMaterial(nuevo_material)
                                    elif mod == 4:
                                        nuevo_sistema_fijacion = validar_alfanumerico("Introduzca el nuevo sistema de fijación:  ")
                                        bioinstrumento.setMaterial(nuevo_sistema_fijacion)
                                    elif mod == 5:
                                        nueva_fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la nueva fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')
                                        bioinstrumento.setFecha_mantenimiento(nueva_fecha_mantenimiento)
                                        
                                elif bioinstrumento.getTipo_bioinstrumento() == "protesis_rodilla":
                                    mod = validar_entero("""--Modificación--
                                                        \r1. Estado
                                                        \r2. Tamaño
                                                        \r3. Material
                                                        \r4. Tipo de Fijación
                                                        \r5. Fecha de mantenimiento 
                                                        \r:   """)
                                    fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
                                    bioinstrumento.setFecha_revision(fecha_revision)
                                    if mod == 1:
                                        nuevo_estado = validar_alfanumerico("Introduzca el nuevo estado del marcapasos cardiaco:  ")
                                        bioinstrumento.setEstado(nuevo_estado)
                                    elif mod == 2:
                                        nuevo_tamaño = validar_alfanumerico("Introduzca el nuevo tamaño:  ")
                                        bioinstrumento.setTamaño(nuevo_tamaño)
                                    elif mod == 3:
                                        nuevo_material = validar_alfanumerico("Introduzca el nuevo material:  ")
                                        bioinstrumento.setMaterial(nuevo_material)
                                    elif mod == 4:
                                        nuevo_tipo_fijacion = validar_alfanumerico("Introduzca el nuevo tipo de fijación:  ")
                                        bioinstrumento.setTipo_fijacion(nuevo_tipo_fijacion)
                                    elif mod == 5:
                                        nueva_fecha_mantenimiento = datetime.datetime.strptime(input("Ingrese la nueva fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')
                                        bioinstrumento.setFecha_mantenimiento(nueva_fecha_mantenimiento)
                        break

                    elif vbio == 4:
                        print("--Registro completo de bioinstrumentos--".center(90))
                        for bioinstrumento in registro[paciente]:
                            tipo_bio = bioinstrumento.getTipo_bioinstrumento()
                            if tipo_bio == "protesis_cadera":
                                print("Protesis de cadera".center(50))
                                print(f"""Medico: {bioinstrumento.getMedico()}
                                         \rEstado: {bioinstrumento.getEstado()}
                                         \rTamaño (En cm): {bioinstrumento.getTamaño()}
                                         \rMaterial: {bioinstrumento.getMaterial()}
                                         \rTipo de fijacion: {bioinstrumento.getTipo_fijacion()}
                                         \rFecha de la ultima revision: {bioinstrumento.getFecha_revision()}
                                         \rFecha del siguiente mantenimiento: {bioinstrumento.getFecha_mantenimiento()}
                                         \rFecha de implantacion del bioinstrumento: {bioinstrumento.getFecha_implante()}""")
                                continue
                            
                            elif tipo_bio == "marcapasos_cardiaco":
                                print("Marcapasos cardiaco".center(50))
                                print(f"""Medico: {bioinstrumento.getMedico()}
                                         \rEstado: {bioinstrumento.getEstado()}
                                         \rNúmero de electrodos: {bioinstrumento.getN_electrodos()}
                                         \rAlambrico o inalambrico: {bioinstrumento.getAlam_inal()}
                                         \rFrecuencia de estimulacion (en segundos): {bioinstrumento.getFrecuencia_estimulacion()}
                                         \rFecha de la ultima revision: {bioinstrumento.getFecha_revision()}
                                         \rFecha del siguiente mantenimiento: {bioinstrumento.getFecha_mantenimiento()}
                                         \rFecha de implantacion del bioinstrumento: {bioinstrumento.getFecha_implante()}""")
                                continue

                            elif tipo_bio == "stents_coronarios":
                                print("Protesis de cadera".center(50))
                                print(f"""Medico: {bioinstrumento.getMedico()}
                                        \rEstado: {bioinstrumento.getEstado()}
                                        \rLongitud (En cm): {bioinstrumento.getLongitud()}
                                        \rDiametro: {bioinstrumento.getDiametro()}
                                        \rMaterial: {bioinstrumento.getMaterial()}
                                        \rFecha de la ultima revision: {bioinstrumento.getFecha_revision()}
                                        \rFecha del siguiente mantenimiento: {bioinstrumento.getFecha_mantenimiento()}
                                        \rFecha de implantacion del bioinstrumento: {bioinstrumento.getFecha_implante()}""")
                                continue
                            
                            elif tipo_bio == "implantes_dentales":
                                print("Marcapasos cardiaco".center(50))
                                print(f"""Medico: {bioinstrumento.getMedico()}
                                         \rEstado: {bioinstrumento.getEstado()}
                                         \rForma del bioinstrumento: {bioinstrumento.getForma()}
                                         \rMaterial: {bioinstrumento.getMaterial()}
                                         \rSistema de fijacion: {bioinstrumento.getSistema_fijacion()}
                                         \rFecha de la ultima revision: {bioinstrumento.getFecha_revision()}
                                         \rFecha del siguiente mantenimiento: {bioinstrumento.getFecha_mantenimiento()}
                                         \rFecha de implantacion del bioinstrumento: {bioinstrumento.getFecha_implante()}""")
                                continue
                            
                            elif tipo_bio == "protesis_rodilla":
                                print("Marcapasos cardiaco".center(50))
                                print(f"""Medico: {bioinstrumento.getMedico()}
                                         \rEstado: {bioinstrumento.getEstado()}
                                         \rTamaño: {bioinstrumento.getTamaño()}
                                         \rMaterial: {bioinstrumento.getMaterial()}
                                         \rTipo de fijación: {bioinstrumento.getTipo_fijacion()}
                                         \rFecha de la ultima revision: {bioinstrumento.getFecha_revision()}
                                         \rFecha del siguiente mantenimiento: {bioinstrumento.getFecha_mantenimiento()}
                                         \rFecha de implantacion del bioinstrumento: {bioinstrumento.getFecha_implante()}""")
                                continue

                    elif vbio == 5:
                        print("Volviendo al menu principal")
                        break
                    else:
                        print("Elija una de las opciones indicadas")

        elif menu == 3:
            print("--Revisión de estado de bioinstrumentos--".center(90))
            n_registro = validar_entero("Introduzca el número de registro del bioisntrumento: ")
            for paciente in registro.keys():
                for bioinstrumento in registro[paciente]:
                    if n_registro == bioinstrumento.getN_registro():
                        print(f"""El bioisntrumento que consulta tiene el siguiente estado: {bioinstrumento.getEstado()}
                                \rSe le tiene asignada la siguiente fecha de mantenimiento: {bioinstrumento.getFecha_mantenimiento()}""")


        elif menu == 4:

            print("--Vuelva pronto--")
            break

if __name__ == "__main__":
  main()