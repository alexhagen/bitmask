.PHONY: docs
docs:
	sphinx-build -M html doc/source doc/build
	#sphinx-build -M latexpdf doc/source doc/build


.PHONY: test
test:
	pytest -v --ignore=sandbox/ --cov=./ --cov-branch --cov-report=html --cov-config=.coveragerc test/ | tee doc/source/_static/doc_test.txt


.PHONY: lint
lint:
	pylint bitmask || true
