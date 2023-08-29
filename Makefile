.PHONY: build clean install

build:
	pyinstaller scripts/run.py \
		--add-data="assets:assets" \
		--add-data="pyjam.toml:." \
        --onefile \
        --name pyjam

clean:
	rm -fr ./build
	rm -fr ./dist
	rm ./*.spec

install:
	pip install -e .
