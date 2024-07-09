#!/bin/bash
#script to display status code
curl -s "$1" | wc -c
