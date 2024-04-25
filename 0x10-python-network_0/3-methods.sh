#!/bin/bash
# displays the HHTP methods the server accepts
curl -s -I "$1" | grep -i "^Allow:" | tr -d '\r' | cut -d ' ' -f 2-
