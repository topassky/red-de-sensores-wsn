# -*- coding: utf-8 -*-
import csv


def usuario():
	infile = csv.reader(open('configuraciones/usuario.conf', 'r'))
	#	usuario.conf consta de Numero de nodos(0-99), 0  2
        #	Periodo de muestreo(minutos),                 1  0.1
        #	Tiempo de espera(Segundos), 		      2  7
        #	nro.de intentos por nodo                      3  3
	for line in infile:
	    msg=line
	return msg

def general():
	infile = csv.reader(open('configuraciones/general.conf', 'r'))
	#	general.conf consta de un Numero de variables 
	#	necesarias para ejecutar el software
	for line in infile:
	    msg=line
	return msg

def Nodo(n):
	ruta='configuraciones/nodo'+str(n)+'.conf'
	infile = csv.reader(open(ruta, 'r'))
	#	La configuraciòn de los nodos solo tiene un paràmetro por nodo, 
	#	el segundo paràmetro es la cifra X 
	#	que acompaña el nombre del archivo: nodoX.conf
	for line in infile:
	    msg=line
	return msg 



	