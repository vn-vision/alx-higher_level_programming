#!/bin/bash
# This script takes in a url, sends DELETE request to the url
curl -s -X DELETE "$1"
