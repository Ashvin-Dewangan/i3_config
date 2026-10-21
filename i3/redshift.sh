#!/bin/bash

# The normal temp is 6500K and yellow light is to be 5500K, time 30min.
Change=1000
Time=10 
Date=$(date +"%H")
Date=$(($Date))
# The $(()) is to convert data in int
Temp=6500
while true; do
	if [ $Date -ge 19 ] && [ $Date -le 20 ]; then
		redshift -PO $Temp
		for (( i=1; i<=$Time; i++ )); do
			sleep 1m
			Temp=$(($Temp + $Change/$Time))
			redshift -PO $Temp
		done
	elif [ $Date -ge 6 ] && [ $Date -le 7 ]; then
		redshift -PO $Temp-$Change
		for (( i=1; i<=$Time; i++ )); do
			sleep 1m
			Temp=$(($Temp + $Change/$Time))
			redshift -PO $Temp
		done
	else
		sleep 1m
	elif [ $Date -ge 20 ]; then
		redshift -PO $Temp-$Change
	elif [ $Date -ge 7 ]; then
		redshift -PO $Temp
	fi
	# notify-send "working"
done
