#!/bin/bash
#script to display content that sent delete reques
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
