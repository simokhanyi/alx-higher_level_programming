#!/bin/bash
#bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
[ $# -eq 1 ] && curl -sH "X-School-User-Id: 98" "$1"
