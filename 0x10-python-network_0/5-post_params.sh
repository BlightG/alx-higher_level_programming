#!/bin/bash
# post to a passed url
curl -s -X POST "$1" -H "email:	test@gmail.com" -H "subject: I will always be here for PLD"
