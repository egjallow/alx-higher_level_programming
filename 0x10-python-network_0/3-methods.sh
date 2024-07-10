#!/bin/bash
#script to display content that sent delete reques
curl -sI "$1"| grep "Allow"| cut -d " " -f 2-
