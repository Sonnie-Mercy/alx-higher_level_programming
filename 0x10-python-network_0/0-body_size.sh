#!/bin/bash
# script takein a URL, sends a request and displays the body of the response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
