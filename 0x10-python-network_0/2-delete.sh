#!/bin/bash
# Sends a DELETE request to the URL passed as the first arg
curl -s "$1" -X DELETE
