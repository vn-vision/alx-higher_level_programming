#!/usr/bin/env bash
# This script displays the content-leght of the response 
# It takes url as a parameter

if [ "$#" -eq 1 ]; then
	curl -s -I "$1" | grep Content-Length | sed 's/[^0-9]*//g'
fi
