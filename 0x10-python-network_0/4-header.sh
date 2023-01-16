#!/bin/bash
# get request sets header variable 
curl -s -X Set-Cookie: X-School-User-Id=98 "$1" 
