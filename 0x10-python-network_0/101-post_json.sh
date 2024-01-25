#!/bin/bash
#bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
[ $# -eq 2 ] && url=$1 && json_file=$2 && curl -sX POST -H "Content-Type: application/json" -d "@$json_file" "$url"
