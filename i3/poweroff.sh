#!/bin/bash

for time in 3 2 1
do
	notify-send "Powering Off in $time sec"
	sleep 1
done
systemctl poweroff
