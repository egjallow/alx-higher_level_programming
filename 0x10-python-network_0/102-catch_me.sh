#!/bin/bash
#script to display content that sent  json postrequest
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
