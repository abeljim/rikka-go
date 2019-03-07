
all: client server

client:
	go get
	protoc rikka.proto --go_out=plugins=grpc:.

server:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. rikka.proto

test:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. rikka.proto

clean:
	rm -f rikka.pb.go

docker: docker-build docker-run

docker-build:
	docker build -t puradox/rikka:1.2.1 -t puradox/rikka:latest .

docker-run:
	docker run -it puradox/rikka:latest

publish: docker-build
	docker push puradox/rikka:1.2.1
	docker push puradox/rikka:latest
