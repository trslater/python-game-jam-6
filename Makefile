.PHONY: build install

build:
	pyinstaller scripts/run.py \
        --onefile \
        --name pyjam

install:
	pip install -e .
