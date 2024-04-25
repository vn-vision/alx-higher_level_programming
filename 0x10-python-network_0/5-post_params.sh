#!/bin/bash
# this scripts sends POST request with data to body
curl -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -s "$1"
