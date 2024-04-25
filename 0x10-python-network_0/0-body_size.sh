#!/bin/bash
# This script displays the content-leght of the response 
curl -s "$1" | wc -c
