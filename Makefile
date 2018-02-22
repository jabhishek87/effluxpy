.PHONY: doc clean pep8 coverage travis

test: pep8 flake8 eslint
	python -c 'import yaml;yaml.load(open(".travis.yml").read())'
ifdef debug
	python setup.py test --debug=$(debug)
else
	python setup.py test
endif

clean:
	rm -rf build dist effluxpy.egg-info htmlcov MANIFEST \
	       .eggs *.egg .coverage
	find effluxpy -type f -name "*.py[co]" -delete
	find effluxpy -type d -name "__pycache__" -delete
	$(MAKE) -C docs/docs_builder clean

build-env:
	mkdir -p build
	python3 -m venv build/env3
	build/env3/bin/pip install pip --upgrade
	build/env3/bin/pip install wheel

build: clean build-env
	build/env3/bin/python setup.py bdist_wheel
	build/env3/bin/python setup.py sdist

upload: clean build-env
	build/env3/bin/python setup.py bdist_wheel upload
	build/env3/bin/python setup.py sdist upload

doc:
	$(MAKE) -C docs/docs_builder html 2>&1 | grep -v \
		'WARNING: more than one target found for cross-reference'
	cp -rv docs/docs_builder/.build/html/* docs/

showdoc: doc
	xdg-open file://${CURDIR}/docs/docs_builder/.build/html/index.html >> /dev/null

pep8:
	find effluxpy -type f -name "*.py" -exec pep8 --ignore=E123,E126,E121 {} +

eslint:
	eslint \
		--ignore-path .gitignore \
		--ignore-pattern *.min.js \
		${CURDIR}/effluxpy

flake8:
	flake8 effluxpy/

coverage:
	coverage run --source=effluxpy setup.py test

showcoverage: coverage
	coverage html
	xdg-open file://${CURDIR}/htmlcov/index.html >> /dev/null

travis-script: pep8 flake8 coverage

travis-script-sphinx:
	travis-sphinx --nowarn --source=doc build

travis-success:
	codecov
	coveralls

travis-success-sphinx:
	travis-sphinx deploy
