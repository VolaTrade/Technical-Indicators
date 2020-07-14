package:
	python setup.py sdist
	python setup.py bdist_wheel
	rm -rf cython_indicators-*.*.*-cp37-cp37m-linux_x86_64.whl

test:
	python -m pytest