from Cython.Distutils import build_ext
import setuptools
import os 
from setuptools import Extension
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = 'requirements.txt'
install_requires = [] 
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
cmdclass = {}
ext_modules = [Extension("indicators", ["src/indicators.pyx"])]
cmdclass.update({'build_ext': build_ext})

setuptools.setup(
    name="cython_indicators", 
    version="0.0.3",
    author="Ethen Pociask",
    author_email="epociask@volatrade.com",
    description="Indicator functions using cython",
    long_description="TO BE ADDED",
    long_description_content_type="text/markdown",
    url="https://github.com/epociask/cython_indicator_functions.git",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass = cmdclass,
    ext_modules = ext_modules,

)

