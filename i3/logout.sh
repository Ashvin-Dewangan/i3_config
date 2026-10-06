#! /bin/bash

for time in 3 2 1
do
	notify-send "Logging Out in $time sec"
	sleep 1
done
i3-msg exit
