
all: client

client: rikka.proto
	go get
	protoc rikka.proto --go_out=plugins=grpc:.

test:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. rikka.proto

clean:
	rm -f rikka.pb.go
