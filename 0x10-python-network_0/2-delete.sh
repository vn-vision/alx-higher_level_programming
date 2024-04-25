#!/bin/bash
# This script takes in a url, sends DELETE request to the url
curl -s -I -X DELETE "$1"
