#!/bin/bash
# script send a request to URL and dispalys this of the respones's body

curl -sIL 54.144.137.83 | grep Content-Length | sed 's/Content-Length: //'
