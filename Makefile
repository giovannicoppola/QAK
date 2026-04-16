.PHONY: build db summaries install clean all

BINARY = qak
DB = qak.db

all: db summaries build

build:
	CGO_ENABLED=1 GOOS=darwin GOARCH=arm64 go build -o $(BINARY)-arm64 ./cmd/qak
	CGO_ENABLED=1 GOOS=darwin GOARCH=amd64 go build -o $(BINARY)-amd64 ./cmd/qak
	lipo -create $(BINARY)-arm64 $(BINARY)-amd64 -output $(BINARY)
	rm -f $(BINARY)-arm64 $(BINARY)-amd64

db:
	python3 scripts/build_qak_db.py

summaries:
	python3 scripts/generate_summaries.py

install: build
	cp $(BINARY) /usr/local/bin/$(BINARY)

clean:
	rm -f $(BINARY) $(DB)
