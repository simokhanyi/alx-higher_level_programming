#!/bin/bash
#bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
[ $# -eq 1 ] && url=$1 && curl -s -o /dev/null -w "%{http_code}" "$url"
