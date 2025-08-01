all: clean wot.svg wot-full.svg index.html index-full.html generate-WKD

generate-WKD: staffs.json
	mkdir -p ./.well-known/openpgpkey
	cd ./.well-known && ./make.py ../staffs.json

wot.svg wot-full.svg: staffs.json
	./wot.py ./staffs.json

index.html: index.md wot.svg
	nix run nixpkgs#pandoc -- -c style.css --standalone index.md -o index.html --to=html5 --metadata title="Web Key Directory of AOSCC 2025" -V lang=en-US

index-full.html: index-full.md wot-full.svg
	nix run nixpkgs#pandoc -- -c style.css --standalone index-full.md -o index-full.html --to=html5 --metadata title="Web Key Directory of AOSCC 2025 (Full Version)" -V lang=en-US

.PHONY: clean
clean:
	rm -rf index.html index-full.html
	rm -rf ./.well-known/openpgpkey
	rm -rf wot.svg wot-full.svg
