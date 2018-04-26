# peigen
Python wrapper for Eigen C++ headers

To use, include the following in your `setup.py` file:

```python
from peigen import header_path
```

For example, if you are using `pybind11` the following code should be contained in your `setup.py`:

```python
from setuptools import setup, Extension

import peigen

ext_modules = [
    Extension(
        'scarlet.operators_pybind11',
        ['scarlet/operators_pybind11.cc'],
        include_dirs=[
            get_pybind_include(),
            get_pybind_include(user=True),
            eigen.header_path
        ],
        language='c++'
    )
]

setup(
  name = 'pkgname',
  ext_modules=ext_modules,
)
```