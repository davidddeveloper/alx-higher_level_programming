#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
url="$1"

response_size=$(curl -s -o /dev/null -w "%{size_download}" $url)
echo "$response_size"
