#!/bin/bash
# This script takes in a url, sends GET request to the url
# displays the HHTP methods the server accepts

# Check if the script is called with exactly one argument (the URL)
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <url>"
    exit 1  # Exit with an error status
fi

# Store the URL provided as the first argument
url="$1"

# Use curl to send a GET request (-I option sends a HEAD request)
# to fetch the headers of the URL and then filter the 'Allow' header
# which specifies the HTTP methods accepted by the server
allowed_methods=$(curl -s -I "$url" | grep -i "^Allow:" | tr -d '\r' | cut -d ' ' -f 2-)

# Check if the 'Allow' header was found
if [ -n "$allowed_methods" ]; then
    echo "Allowed HTTP methods for $url: $allowed_methods"
else
    echo "Unable to determine allowed HTTP methods for $url"
fi

