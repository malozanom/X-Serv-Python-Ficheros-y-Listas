#!/usr/bin/python3

# Miguel Ángel Lozano Montero.
# Programa que obtiene de /etc/passwd la lista de usuarios, la guarda en un
# diccionario y muestra los valores para 'root' e 'imaginario'.

fich = open ("/etc/passwd", "r")
lineas = fich.readlines ()
fich.close ()

usuarios = {}
for linea in lineas:
	elementos = linea.split (':')
	usuarios [elementos [0]] = elementos [-1] [:-1]

try:
	print ("El usuario root utiliza la shell " + usuarios ["root"])
	print ("El usuario imaginario utiliza la shell " + usuarios ["imaginario"])

except KeyError:
	print ("El usuario imaginario no se ha encontrado")

