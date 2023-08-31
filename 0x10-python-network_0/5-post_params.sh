#!/bin/bash
# taskes URL, sends POST request and displaays the body of response
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
