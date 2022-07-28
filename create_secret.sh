#!/usr/bin/bash
ENDPOINT="air-quality-by-api-ninjas.p.rapidapi.com"
API_KEY=YOUR_API_KEY  #PUT YOUR API KEY HERE

kubectl create secret generic api-secret --from-literal=API_HOST="$ENDPOINT" --from-literal=API_KEY="$API_KEY"
