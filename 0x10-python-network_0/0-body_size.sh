#!/bin/bash
# This script displays the content-leght of the response 
# It takes url as a parameter

curl -s -I "$1" | grep Content-Length | sed 's/[^0-9]*//g'
