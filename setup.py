from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
parent_directory = path.dirname(this_directory)
with open(path.join(parent_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'quantumdl',
  packages = ['quantumdl'],
  version = '0.1.1',
  license='Apache License 2.0',
  description = 'A Quantum Deep Learning Library!',
  author = 'Debabrata Roy Chowdhury',
  author_email = 'debabrata.rc@dexterai.com',
  url = 'https://github.com/dexterai-lab/quantumdl',
  download_url = 'https://github.com/dexterai-lab/quantumdl/archive/v0.1-alpha.tar.gz',
  keywords = ['QUANTUM COMPUTING', 'DEEP LEARNING', 'ARTIFICIAL INTELLIGENCE', 'PYTHON' ],
  python_requires=('>=3.6.0'),
  install_requires=['cirq'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: Apache Software License'
  ],
)