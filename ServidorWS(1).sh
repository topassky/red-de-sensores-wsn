#!/bin/sh
### BEGIN INIT INFO
# Provides:          Comcop
# Required-Start:    $syslog 
# Required-Stop:     $syslog 
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# X-Interactive:     true
# Short-Description: 
# Description:       
#  
### END INIT INFO
 
sh /ServidorISA/ServidorWSN/Ejecutar.sh
 
exit
