import serial
import time

def Solicitar(nodo, ConfigNodo):  ####   Tx
	#	Trnasmitir los dos parametros que tengo: nodo y configuraciones 
	#  	por el puerto serial con el formato prestablecido
	#	 # xx , yy #    //sin espacios
	if (nodo < 10):
		strnodo='0'+str(nodo)
	else:
		strnodo=str(nodo)
	if len(ConfigNodo[0])==1:
		strconfignodo='0'+ConfigNodo[0]
	else :
		strconfignodo=ConfigNodo[0]

	
	port = '/dev/ttyACM0'
	ard = serial.Serial(port,9600,timeout=5)
	ard.write('#'+strnodo+','+strconfignodo+'#')
	time.sleep(0.1)

	print('transmitiendo )))))))#'+strnodo+','+strconfignodo+'#')
	return 0