{
  "name": "ido-lister",
  "version": "1.0.0",
  "description": "List of upcoming and active IDOs",
  "main": "index.js",
  "scripts": {
    "start": "parcel index.html",
    "build": "parcel build index.html --public-url ./",
    "deploy": "vercel --prod"
  },
  "dependencies": {
    "@fortawesome/fontawesome-free": "^5.15.4",
    "parcel-bundler": "^1.12.5",
    "tailwindcss": "^2.2.17",
    "web3": "^1.6.0"
  }
}
