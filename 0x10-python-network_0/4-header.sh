#!/bin/bash
# this script sends GET request and displays the response
curl -X GET -d "X-School-User-Id=98" -s "$1"
