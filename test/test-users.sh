curl -v http://127.0.0.1:8081/page/ -H 'x-api-key: 1234' --data @twitter.json
sleep 30
curl -v http://127.0.0.1:8081/page/ -H 'x-api-key: 1234' --data @github.json
sleep 30
curl -v http://127.0.0.1:8081/page/ -H 'x-api-key: 1234' --data @medium.json
