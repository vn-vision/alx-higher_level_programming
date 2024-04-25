#!/bin/bash
# This script displays the content-leght of the response 
curl -s "$1" | grep Content-Length | sed 's/[^0-9]*//g'
