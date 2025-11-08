# A proof of concept app "Command trigger"
This is POC app, that shows that it's possible to trigger a command on a Linux machine remotely with a backend app via HTTP.

## How to install
Install Docker on your machine first. Then you can use Docker to start the whole application:
```bash
docker compose up --build
```
## Usage
 Send HTTP requests to the backend. You can use `curl` as shown below. Or use GUI Postman app for API requests: 
```bash
curl -X POST http://localhost:5001/run \
     -H "Content-Type: application/json" \
     -d '{"cmd":"ls /"}'

curl -X POST http://localhost:5001/run \
     -H "Content-Type: application/json" \
     -d '{"cmd":"echo hello world"}'

curl -X POST http://localhost:5001/run \
     -H "Content-Type: application/json" \
     -d '{"cmd":"bash --version"}'
```

Created by Lev Nagornov.
