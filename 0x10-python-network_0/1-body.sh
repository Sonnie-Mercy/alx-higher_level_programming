#!/bin/bash
# takes URL, sends GET, displays the body of the response
curl -sL "$1" -X GET
