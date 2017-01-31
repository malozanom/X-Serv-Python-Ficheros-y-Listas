#!/usr/bin/python3

# Miguel Ángel Lozano Montero.
# Programa que obtiene de /etc/passwd la lista de usuarios y la shell que usa.

fich = open ("/etc/passwd","r")
lineas = fich.readlines ()
fich.close ()

# Existen 3 formas de hacerlo:

#for linea in lineas:
#	pos_fin = linea.find (':')
#	login = linea [:pos_fin]
#	pos_com = linea.rfind (':')
#	shell = linea [pos_com + 1:-1]
#	print (login,shell)

#print ("El numero de usuarios es " + str (len (lineas)))


for linea in lineas:
	elementos = linea.split (':')
	login = elementos [0]
	shell = elementos [-1]
	shell_bueno = shell [:-1]
	print ("Usuario:" + login + " Shell:" + shell_bueno)

print ("El numero de usuarios es " + str (len (lineas)))


#for linea in lineas:
#	login = linea.split (':')[0]
#	shell = linea.split (':')[-1][:-1]
#	print (login, shell)

#print ("El numero de usuarios es " + str (len (lineas)))

