#!/bin/bash
# This script takes in a url, sends GET request to the url
# displays the body only if the status code is 200 ok

curl -sL "$1"
