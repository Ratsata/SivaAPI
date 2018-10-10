from pyfcm import FCMNotification
import os, os.path
import subprocess
import time
import json

push_service = FCMNotification(api_key="AAAA2QerSj8:APA91bGfLqEstIT16uZvIi9uy68GlGV-PmKxcQs7eWzHcw1XETEXfiRNExy2iEDg7tTFF6JQo49iiBbUSx5vEj7a7o2TNboDzaYCi9ZHPEkW1IOA0-Qi2wKy-UjisglHNQlUdRaMTjJ8vWqxJhn9wv_9tT1skVVzJw")
message_title = "Alerta de movimiento!"
message_body = "La camara SIVA ha detectado movimiento"
sound = "default"

f=open("topics.json", "r")
if f.mode == 'r':
	file = json.loads(f.read())
	for i in file:
		result = push_service.notify_topic_subscribers(topic_name=i["nombre"], message_title = message_title, message_body = message_body, sound = sound)
		print result
