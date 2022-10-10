docker build -t test/myapp .
docker stop myapi
docker rm myapi
docker run -d --name myapi -p 80:80 test/myapp
sleep .5; python3 -m unittest tests/test_api.py

