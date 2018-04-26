#7.- La idea es hacer dos módulos el primer módulo deberá crear una función que cree un listado de datos, los datos a guardar serán de una clase llamada Cliente
from modelo import Cliente,creaClientes

#8.- La clase cliente estará en el módulo llamado modelo, y dispondrá de los datos: nombre, dirección, tlf, email y facturación anual

#9.- El segundo módulo se llamará procesado y tendrá que tener una función que sea capaz de devolver el total de la facturación de la
# empresa sumando todos los totales de facturación anual de los clientes


def facturacionTotal(listado):
    suma=0
    for cliente in listado:
        suma = suma + cliente.factanual
    return suma


#10.- Crea una función más en el módulo de procesado que deberán devolver la media  de la facturación por cliente

def mediaFacturacionTotal(listado):
    suma=0
    clientes=0
    for cliente in listado:
        clientes = clientes +1
        suma = suma + cliente.factanual
    return suma/clientes

def mediaFacturacionTotalVaga(listado):
    ftotal=facturacionTotal(listado)
    return ftotal/ len(listado)


#11.-  El programa principal deberá importar los dos módulos, deberá llamar a la función que devuelve el listado de clientes ya rellenados y deberá llamar a las funciones que devuelvan la facturación total y la media de facturación por cliente