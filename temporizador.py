# -*- coding: utf-8 -*-
import time
import sys,os
import Configuracion
import Recolector
import Consulta
import datetime
import Alerta
####Ejecuciòn ppal





def Solicitud(CONFIG,start):
	if ((time.time()-start) > (float(CONFIG[1])*60)):####Ciclo que se repite cada que el periodo lo estime
		for x in range (int(CONFIG[0])): #########Ciclo que se repite deacuerdo al nùmero de nodos
			nodo=x+1
			print('======================')
			for intento in range (int(CONFIG[3])):#########Ciclo que se repite deacuerdo al nùmero de intentos
				print('======================')				
				print('Nodo: '+str(nodo)+'---Intento: '+str(intento+1))				
				Consulta.Solicitar(nodo, Configuracion.Nodo(nodo))#( TX y reinicio  timer")	
				Flag=Recolector.Toma(nodo,int(CONFIG[2]))   #  RX 
				start2 = time.time()
				if Flag==0:
					break
				else:
					if intento ==int(CONFIG[3])-1:
						Alerta.crear(nodo,': Despues del numero de intentos especificados por el usuario(usuario.conf), no se ha obtenido respuesta del servidor remoto(nodo), por favor chequee estado de bateria, conexiones, tiempo de espera o nùmero de intentos, además de otras posibles causas de esta falla, si continua, por favor comunìquese con el proveedor del software para mas informaciòn y entregue el sieguiente còdigo de error: SISA01\n\n')
			if nodo==int(CONFIG[0]):
				#os.system('del *.zip')
				os.system('zip -r /var/www/html/'+AA+MM+DD+'-'+HH+':'+Mi+'.zip Datos')	 

		print(time.time()-start) 
		print('==Se procede con el sig. intento==')	
		start = time.time()
	return start

def Muestreo():
	print ('muestreo')
	start = time.time()
	x=Configuracion.general()
	if (int(x[0])==0):
		x[0]='1'
		d='1'
		for i in range((len(x)-1)):			##CAmbiar el primer campo por 1 para poder empezar a ejecutar el software
			d=d+','+x[i+1]
			os.system('echo ' +d+'>configuraciones/general.conf')
			
		#os.system(comando)
	while((x[0])=='1'):###ciclo infinito
		#os.system('echo 7,0.09,7,3>general.conf')
		AA=str(datetime.datetime.now().year)
		DD=str(datetime.datetime.now().day)
		MM=str(datetime.datetime.now().month)
		HH=str(datetime.datetime.now().hour)
		Mi=str(datetime.datetime.now().minute)	
		start=Solicitud(Configuracion.usuario(),start)##Ejemplo de la funcion solicitud, se hace  la peticiòn en minutos
		x=Configuracion.general()

	return 0

Muestreo()