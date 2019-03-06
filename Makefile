
all: client

client: rikka.proto
	go get
	protoc rikka.proto --go_out=plugins=grpc:.

clean:
	rm -f rikka.pb.go
