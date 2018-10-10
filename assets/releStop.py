#!/usr/bin/python
#Archivo:         releStop.py
#Programa:        SivaAPI
#Proyecto:        Siva
#Autor:           Sebastian Vega
#
#===========================================
#Fecha      |  Programador        | Detalles
#===========================================
#10-09-18      Sebastian Vega       Creacion

import RPi.GPIO as GPIO
import os

os.system('pkill -f releStart.py')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, False);

GPIO.cleanup()
