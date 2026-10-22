#!/bin/bash
notify-send "☀️ $(fish -c 'math (brightnessctl get)/(brightnessctl max) x 100')"
