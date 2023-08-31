#!/bin/bash
# This script sends a request to the given URL and displays response size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
