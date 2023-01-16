#!/bin/bash
# list all options from server
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
