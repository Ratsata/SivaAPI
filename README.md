# SivaAPI

  Api escrita en PHP para controlar el equipo Siva desde la App Mobil.

## Metodos

 - Alarma: *alarm(string tipo)*
 Activa una alarma dependiendo el tipo de alarma ingresado

        upload.php?action=alarm&tipo=emergencia

 - Voice: *alarm()*
 Envia un audio para ser reproducido por el equipo Siva

        upload.php?action=voice

 - Stop: *stop()*
 Detiene la alarma activada

        upload.php?action=stop

 - getPID: *getPID(string nameOfPID)*
 Obtiene el PID del nombre entregado

        upload.php?action=getPID

 - get: *get()*
 Obtiene el listado de los topicos subscritos

        upload.php?action=get

 - add: *add(string id)*
 Crea un nuevo topico

        upload.php?action=add&id=SIVA01

 - remove: *alarm(string id)*
 Remueve un topico

        upload.php?action=remove&tipo=SIVA01

