import datetime as datetime
from validaciones import *
fecha_mantenimiento = datetime.datetime.strptime(validar_alfabetico("Ingrese la fecha de mantenimiento en formato DD/MM/YY: "), '%d/%m/%Y')
#fecha_revision = datetime.datetime.now().strftime("%d/%m/%Y")
print(fecha_mantenimiento)