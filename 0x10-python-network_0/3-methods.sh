#!/bin/bash
#script to display content that sent delete reques
curl -sI "$1" | awk '/^Allow/{$1=""; print $0}' | sed 's/^ //'
