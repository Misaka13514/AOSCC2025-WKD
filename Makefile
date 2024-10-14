all: clean wot.svg index.html generate-WKD

generate-WKD: staffs.json
	mkdir -p ./.well-known/openpgpkey
	cd ./.well-known && ./make.py ../staffs.json

wot.svg: staffs.json
	./wot.py ./staffs.json

index.html: index.md wot.svg
	nix run nixpkgs#pandoc -- -c style.css --standalone index.md -o index.html --to=html5 --metadata title="Web Key Directory of Project Trans" -V lang=en-US

.PHONY: clean
clean:
	rm -rf index.html
	rm -rf ./.well-known/openpgpkey
	rm -rf wot.svg
