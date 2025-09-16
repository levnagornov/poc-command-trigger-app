docker compose up --build

curl -X POST http://localhost:5001/run \
     -H "Content-Type: application/json" \
     -d '{"cmd":"ls /"}'

curl -X POST http://localhost:5001/run \
     -H "Content-Type: application/json" \
     -d '{"cmd":"echo hello world"}'

curl -X POST http://localhost:5001/run \
     -H "Content-Type: application/json" \
     -d '{"cmd":"bash --version"}'
