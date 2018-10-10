#!/usr/bin/python
#Archivo:         fcm.py
#Programa:        SivaAPI
#Proyecto:        Siva
#Autor:           Sebastian Vega
#
#===========================================
#Fecha      |  Programador        | Detalles
#===========================================
#10-09-18      Sebastian Vega       Creacion

from pyfcm import FCMNotification
import os, os.path
import subprocess
import time
import json
from urllib2 import urlopen

push_service = FCMNotification(api_key="AAAA2QerSj8:APA91bGfLqEstIT16uZvIi9uy68GlGV-PmKxcQs7eWzHcw1XETEXfiRNExy2iEDg7tTFF6JQo49iiBbUSx5vEj7a7o2TNboDzaYCi9ZHPEkW1IOA0-Qi2wKy-UjisglHNQlUdRaMTjJ8vWqxJhn9wv_9tT1skVVzJw")
message_title = "Alerta de movimiento!"
message_body = "La camara SIVA ha detectado movimiento"
sound = "default"
ipAux = 0
DIR = '/home/pi/mail/new'
PATH = '/var/www/html/upload'
FNULL = open(os.devnull, 'w')
retcode = subprocess.call('getmail', stdout=FNULL, stderr=subprocess.STDOUT)
cantAux = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
ciclo = 0

def checkIP():
	global ipAux
	global PATH
	try:
		ip = urlopen('http://ip.42.pl/raw').read()
		#if ipAux != ip:
		ipAux = ip
		f=open(PATH+"/assets/topics.json", "r")
		file = json.loads(f.read())
		if f.mode == 'r':
			for i in file:
				data = {
				   "type": "ip",
				   "ip": ip,
				   "topic": str(i["nombre"])
				}
				result = push_service.notify_topic_subscribers(topic_name=i["nombre"], data_message=data)
				print 'IPMENSSAGE = Topic:'+str(i["nombre"])+' - Success:'+str(result["success"])+" - Message:"+str(data)
		f.closed
	except Exception as e:
		print 'No internet connection.-'
	return

checkIP()
while True:
	retcode = subprocess.call('getmail', stdout=FNULL, stderr=subprocess.STDOUT)
	cant = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

	if cantAux != cant:
		f=open("topics.json", "r")
		if f.mode == 'r':
			file = json.loads(f.read())
			for i in file:
				result = push_service.notify_topic_subscribers(topic_name=i["nombre"], message_title = message_title, message_body = message_body, sound = sound)
				#result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
				print 'IPMENSSAGE = Topic:'+str(i["nombre"])+' - Success:'+str(result["success"])+" - Message:"+str(message_title)
		f.closed
		for x in range (1,55):
			print x
			time.sleep(1)
			ciclo = 6
		retcode = subprocess.call('getmail', stdout=FNULL, stderr=subprocess.STDOUT)
		cant = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
		cantAux = cant
	if ciclo > 10:
		checkIP()
		ciclo = 0
	time.sleep(5)
	ciclo += 1
