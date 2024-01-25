#!/bin/bash
#script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
[ $# -eq 1 ] && curl -sX DELETE "$1" -d "I'm a DELETE request" | cat
