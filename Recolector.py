# -*- coding: utf-8 -*-
##Programa encargado de guaradar los datos del serial, en la base de datos de mysql
#import ast
import serial
import scanLin
import time
import numpy
import datetime
import Configuracion
import sys, os

AA=str(datetime.datetime.now().year)
DD=str(datetime.datetime.now().day)
MM=str(datetime.datetime.now().month)
HH=str(datetime.datetime.now().hour)
Mi=str(datetime.datetime.now().minute)


def PtoSerial():
	#The following line is for serial over GPIO
	port = '/dev/ttyACM0'
	ard = serial.Serial(port,9600,timeout=5)
	msg = ard.readline()
	return msg

def Toma(nodo, tiempo):
	Flag =1
	msg='*00000,000,00*'
	start = time.time()
	time_elapsed = 0.0
	end = time.time()
	while (time_elapsed<tiempo):##En las lineas mas abajo se comprobarà si la cadena empieza con "("
		time_elapsed = end - start
		# printing information
		#print 'Tiempo de espera:\t{}'.format(time_elapsed)				
		end = time.time()
		################  Conexiòn con serial#
		######################################
		msg=PtoSerial()
		#print msg
		if (len(msg)==15):
			msg1=msg[1:13]
	
			if msg[0]=="*" and msg[13]=="*":#Comprobamos si la cadena empieza con "("
				msg1='('+msg1
				msg1=msg1+')'
				Flag=0
			print 'Tiempo de espera:\t{}'.format(time_elapsed)		
			print('Recibido (((((((((((('+msg1)
		if Flag==0:
			
			os.system('echo '+str(AA)+'-'+str(MM)+'-'+str(DD)+','+str(HH)+':'+str(Mi)+','+msg1[1:13]+'>>Datos/'+str(nodo)+'.csv')
			break
	return Flag