#!/bin/bash
# Script that takes the URL and diplays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
