#!/bin/bash
# Sends a JSON POST request to a URL passed
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
