from procesado import facturacionTotal,mediaFacturacionTotal
from modelo import Cliente,creaClientes

listado=creaClientes()
print(facturacionTotal(listado))
print (mediaFacturacionTotal(listado))