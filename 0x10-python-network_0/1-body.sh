#!/bin/bash
# This script takes in a url, sends GET request to the url
# displays the body only if the status code is 200 ok

if [ "$#" -ne 1  ]; then
	echo "Usage:<file><url>"
else
	# extract the http_code response and the last 3 outputs
	response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
	status_code=${response: -3}

	if [ "$status_code" = "200" ]; then
		# if the status code is 200 ok, display the output
		curl -s -X GET "$1"
	else
		echo "Error: HTTP status_code: $status_code"
	fi
fi
