import os
from setuptools import setup

# Eigen version - peigen version
__version__ = '3.3.4-0.0'

packages = []
for root, dirs, files in os.walk('.'):
    if not root.startswith('./build') and '__init__.py' in files:
        packages.append(root[2:])
print("Packages:", packages)

setup(
  name = 'peigen',
  packages = packages,
  version = __version__,
  description = 'Python wrapper for Eigen C++ header',
  author = 'Fred Moolekamp',
  author_email = 'fred.moolekamp@gmail.com',
  url = 'https://github.com/fred3m/deblender',
  keywords = ['eigen', 'numerical'],
)