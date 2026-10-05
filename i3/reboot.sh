#!/bin/bash

for time in 5 4 3 2 1
do
	notify-send "Rebooting in $time sec"
	sleep 1
done
reboot

