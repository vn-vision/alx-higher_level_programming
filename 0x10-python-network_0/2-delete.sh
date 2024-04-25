#!/bin/bash
# This script takes in a url, sends DELETE request to the url
# displays the body only of the response

if [ "$#" -ne 1  ]; then
	echo "Usage:<file><url>"
else
	curl -X DELETE -s -I "$1"
fi
