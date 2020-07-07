<<<<<<< HEAD
import os 
import subprocess
from setuptools import setup, Extension

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = 'requirements.txt'
install_requires = [] 
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

# cmdclass = {}
# ext_modules = [Extension("indicators", ["src/indicators.pyx"])]
# cmdclass.update({'build_ext': build_ext})
=======
import os
import sys
from setuptools import setup, find_packages
from setuptools.extension import Extension
from setuptools.command.install import install
from Cython.Build import cythonize


VERSION = '0.0.1'

extensions = [
    Extension(
        "indicators",
        ["src/indicators.pyx"],
    )
]


def readme():
    with open('README.md') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = f'Git tag: {tag} does not match the version of this app: {VERSION}'
            sys.exit(info)

>>>>>>> b0f839bf12c0de5ec884f59686fa3f7ae7408872

setup(
    setup_requires=[
            'setuptools>=18.0',
            'cython',
    ],
<<<<<<< HEAD
    name="cython_indicators", 
    version="0.0.6",
=======
    name="cython_indicators",
    version=VERSION,
>>>>>>> b0f839bf12c0de5ec884f59686fa3f7ae7408872
    author="Ethen Pociask",
    author_email="epociask@volatrade.com",
    description="Indicator functions using cython",
    long_description=readme(),
    long_description_content_type="text/markdown",
<<<<<<< HEAD
    url="https://github.com/epociask/cython_indicator_functions.git",
    # packages=setuptools.find_packages(),
    install_requires=install_requires,
=======
    url="https://github.com/VolaTrade/Technical-Indicators",
    install_requires=[
        'Cython==0.29.17',
        'numpy'
    ],
    packages=find_packages(),
>>>>>>> b0f839bf12c0de5ec884f59686fa3f7ae7408872
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Technical Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",

    ],
    python_requires='>=3.6',
<<<<<<< HEAD
    # cmdclass=cmdclass,
    ext_modules=[
        Extension(
            'indicators',
            sources=['src/indicators.pyx'],
        ),
    ],
=======
    cmdclass={
      'verify': VerifyVersionCommand,
    },
    ext_modules=cythonize(extensions)
>>>>>>> b0f839bf12c0de5ec884f59686fa3f7ae7408872
)

