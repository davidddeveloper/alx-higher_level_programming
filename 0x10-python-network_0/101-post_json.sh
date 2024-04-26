#!/bin/bash
# a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
file_content=$(cat "$2")
echo "'$(cat "$2")'"
curl -X POST -H "Content-Type: application/json" -d "'$(cat "$2")'" $1
