#!/bin/bash

# Install Python dependencies
if [[ -f "requirements.txt" ]]; then
  pip install -r requirements.txt
fi

# Install Node dependencies
npm install

# Build Tailwind CSS (no watch flag)
npx tailwindcss -i ./static/src/input.css -o ./static/dist/output.css

# Flask setup (optional — adjust as needed)
export FLASK_APP=app.py
export FLASK_ENV=production

# Only run this in production
if [[ $VERCEL_ENV == "production" ]]; then
  npm run build:production
fi
