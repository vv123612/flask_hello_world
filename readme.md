run localy
python app.py


run
docker build -t my_flask_app:v0.1 . 

docker run --name my_flask_app01 -d -p 5000:5000 my_flask_app:v0.1


run site
http://127.0.0.1:5000/


or check IP by 

docker inspect my_flask_app01 |grep IP

there will be string like that "IPAddress": "172.17.0.2"

http://172.17.0.2:5000/