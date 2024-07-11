#!/bin/bash
#script to display content that sent  json postrequest
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
