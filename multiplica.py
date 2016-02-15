#! /usr/bin/python
#Programa en python que muestra por pantalla las 10 primeras tablas de multiplicar
rango = range(1,11);

for numerando1 in rango:
	cifras = str(numerando1).__len__();
	print("Tabla del " + str(numerando1) + "\n----------" + "-"*cifras);
	for numerando2 in rango:
		print(str(numerando1) + " por " + str(numerando2) + " es " + str(numerando1*numerando2));