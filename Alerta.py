# -*- coding: utf-8 -*-
import datetime
import sys,os

def crear(nodo, mensaje):
	os.system('echo ' + str(datetime.datetime.now())+','+ str(nodo) +','+mensaje +'>>Datos/0.csv')