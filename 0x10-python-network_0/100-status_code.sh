#!/bin/bash
#script to display content that sent delete reques
curl -so /dev/null -w "%{http_code}" "$1"
