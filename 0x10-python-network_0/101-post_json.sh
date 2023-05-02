#!/bin/bash
#sends a JSON post request url and returns the body of the response
curl -s -X POST -H  "Content-Type: application/JSON" -d "@$2" "$1"
