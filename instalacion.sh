#!/bin/bash
# -*- ENCODING: UTF-8 -*-
#importante ServidorWSlo con superusuario




cd Servidor
 
apt-get install apache2
apt-get install php
chmod -R 777 /var/www/html


apt-get install sed
pip install numpy
pip install pyserial

cp Configuracion.php /var/www/html/
mkdir /var/www/html/configuraciones
chmod -R /var/www/html/configuraciones
echo '1,1,1,1'> /var/www/html/configuraciones/general.conf
chmod a=rw /var/www/html/configuraciones/general.conf
echo '1,1'> /var/www/html/configuraciones/nodo.conf
chmod a=rw /var/www/html/configuraciones/nodo.conf

comando="sh "$PWD"/Ejecutar.sh"

echo ' '>>ServidorWS.sh
echo $comando>>ServidorWS.sh
echo ' '>>ServidorWS.sh
echo 'exit'>>ServidorWS.sh

cp ServidorWS.sh /etc/init.d/
chmod +x /etc/init.d/ServidorWS.sh 
update-rc.d ServidorWS.sh defaults
exit 
