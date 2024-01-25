#!/bin/bash
#script that takes in a URL, sends a GET request to the URL, and displays the body 200 of the response
[ $# -eq 1 ] && curl -s -o /dev/stdout -w "%{http_code}" "$1" | awk 'NR>1 {print}'
