#!/usr/bin/python
#Archivo:         playSound.py
#Programa:        SivaAPI
#Proyecto:        Siva
#Autor:           Sebastian Vega
#
#===========================================
#Fecha      |  Programador        | Detalles
#===========================================
#10-09-18      Sebastian Vega       Creacion

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
parser.add_argument("-t", "--type", help="Tipo de alarma a procesar")
args = parser.parse_args()
path = "/var/www/html/upload/assets"
 
if args.file:
	print "El nombre de archivo a procesar es: ", args.file
	os.system("mplayer "+ args.file)
	os.remove(args.file)
else:
	print "Alarma Activada"
#	os.system("mplayer -loop 0 "+ path + "/sounds/alarm_bell.mp3")
	if args.type=='robo':
		os.system("cvlc "+ path +"/sounds/alarm_bell.mp3 --loop")
	if args.type=='incendio':
		os.system("cvlc "+ path +"/sounds/alarm_horn.mp3 --loop")
	if args.type=='emergencia':
		os.system("cvlc "+ path +"/sounds/alarm_submarine.mp3 --loop")
