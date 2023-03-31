#!/bin/bash
# Sends a req to a URL passed as an arg and displays only the status code of the res
curl -s -o /dev/null -w "%{http_code}" "$1"
