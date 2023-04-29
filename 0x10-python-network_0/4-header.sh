#!/bin/bash
# Takes URL as an arg, sends GET, displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
