#!/bin/bash
# this script sends GET request and displays the response
curl -X GET -H "X-School-User-Id: 98" -s "$1"
