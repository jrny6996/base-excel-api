#!/bin/bash
if [[ -f "requirements.txt" ]]; then
  pip install -r requirements.txt

  npm i
  npx @tailwindcss/cli -i ./static/src/input.css -o ./static/dist/output.css --watch

fi



if [[ $VERCEL_ENV == "production"  ]] ; then
  npm run build:production
# else
#   npm run build:preview
# fi