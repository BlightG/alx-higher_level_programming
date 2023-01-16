#!/bin/bash
# sends GET request and displays body for 200 ok response
http_response=$(curl -s -o response.txt -w "%{http_code}" "$1");if [ "$http_response" == "200" ]; then cat response.txt; rm response.txt;fi
