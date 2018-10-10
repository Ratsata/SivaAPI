#!/usr/bin/python
#Archivo:         releStart.py
#Programa:        SivaAPI
#Proyecto:        Siva
#Autor:           Sebastian Vega
#
#===========================================
#Fecha      |  Programador        | Detalles
#===========================================
#10-09-18      Sebastian Vega       Creacion

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
tiempo = .5
while True:
	GPIO.output(17, True);
	time.sleep(tiempo+.2);
	GPIO.output(17, False);
	time.sleep(tiempo);
GPIO.cleanup()
