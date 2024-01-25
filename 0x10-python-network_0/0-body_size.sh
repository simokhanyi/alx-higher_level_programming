#!/bin/bash
#script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
[ $# -eq 1 ] && curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n' || echo "Usage: $0 <URL>"
