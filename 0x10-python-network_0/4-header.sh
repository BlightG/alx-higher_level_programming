#!/bin/bash
# get request sets header variable 
curl -s "$1" -X Set-Cookie: X-School-User-Id=98
