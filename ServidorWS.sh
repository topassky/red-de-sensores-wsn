#!/bin/bash
### BEGIN INIT INFO
# Provides:          COMCOP2016 Carlos-Argoti Juan-Orozco
# Required-Start:    $syslog
# Required-Stop:     $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: blabla
# Description:
#
### END INIT INFO
 
python /home/user/Escritorio/ServidorISA/Servidor/temporizador.py
 
exit
