#! /usr/bin/python
#Programa en python que muestra por pantalla la tabla de multiplicar del numero introducido

tabla = int(raw_input("Introduzca el numero de la tabla a mostrar:"));
rango = range(1,11);
cifras = str(tabla).__len__()	# averigua las cifras que tiene el numero introducido
if tabla <0:
	print("Uso: numero no valido, introduce otro numero (>0)");
else:
	print("Tabla del " + str(tabla) + "\n----------" + "-"*cifras);
	for numero in range(1,11):
		print(str(tabla) + " * " + str(numero) + " = " + str(tabla*numero));