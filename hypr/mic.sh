#!/bin/bash
notify-send "🎤 $(pactl get-source-mute $(pactl get-default-source))"
