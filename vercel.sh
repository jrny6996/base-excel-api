#!/bin/bash
if [[ -f "requirements.txt" ]]; then
  pip install -r requirements.txt
fi



if [[ $VERCEL_ENV == "production"  ]] ; then
  npm run build:production
# else
#   npm run build:preview
# fi