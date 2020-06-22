#Obteniendo paises de Rocketbot
var_rocket = {format}
#Obteniendo el número de índices del arreglo
cantidad = len(var_rocket)
#Iterando arreglo para obtener solo el nombre de los paises
for i in range(cantidad):
	var_rocket[i] = var_rocket[i].split()
	var_rocket[i] = var_rocket[i][0]
#Guardando arreglo con nombre de los paises
SetVar('latpaises',var_rocket)
SetVar('cantidad_paises', cantidad)
