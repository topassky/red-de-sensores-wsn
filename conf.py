# -*- coding: utf-8 -*-

import sys, os
import Configuracion
x=1
while (x>0):
	print('===========================')
	x=input('1-Usuario, 2-Nodo, 0-Salir: ')
	if x==1:
		nn=input('Número de nodos(1-99): ')
		pm=input('Periodo de muestreo(minutos): ')                   
		te=input('Tiempo de espera(Segundos): ')		      
		ni=input('Número de intentos por nodo: ')
		os.system('echo '+str(nn)+','+str(pm)+','+str(te)+','+str(ni)+'>configuraciones/usuario.conf')
	if x==2:
		CONFIG=Configuracion.usuario()
		nodo=input('Número de nodo(1-'+str(CONFIG[0])+',0 para  todos): ')
		on=input('Opción del nodo: ')
		if nodo==0:
			for i in range(int(CONFIG[0])):
				print('Configurado nodo ' + str(i+1)+ ' -> '+ str(on))
				os.system('echo '+str(on)+'>configuraciones/nodo'+str(i+1)+'.conf')					
		else:
			print('Configurado nodo ' + str(nodo)+ ' -> '+ str(on))
			os.system('echo '+str(on)+'>configuraciones/nodo'+str(nodo)+'.conf')