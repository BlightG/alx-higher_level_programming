#!/bin/bash
# script send a request to URL and dispalys this of the respones's body
curl -sIL "$1" | grep Content-Length | sed 's/Content-Length: //'
