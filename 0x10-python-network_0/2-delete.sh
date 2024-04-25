#!/bin/bash
# This script takes in a url, sends DELETE request to the url
curl -X DELETE -s -I "$1"
