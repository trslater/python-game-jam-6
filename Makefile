.PHONY: build clean install

build:
	pyinstaller scripts/run.py \
        --onefile \
        --name pyjam \
		--windowed

clean:
	rm -fr ./build
	rm -fr ./dist
	rm ./*.spec

install:
	pip install -e .
