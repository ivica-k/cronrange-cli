venv: requirements.txt
	test -d venv || virtualenv -p python3 venv
	venv/bin/pip install -Ur dev_requirements.txt

test:
	venv/bin/python -m unittest discover -s cronrange/

tests: test