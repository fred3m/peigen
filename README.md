# peigen
Python wrapper for Eigen C++ headers

To use, include the following in your `setup.py` file:
```python
class get_eigen_include(object):
    """Helper class to determine the peigen include path
    The purpose of this class is to postpone importing peigen
    until it is actually installed, so that the ``get_include()``
    method can be invoked.
    """
    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import peigen
        return peigen.header_path

ext_modules = [
    Extension(
        'your_package.module', # your module that needs the Eigen headers
        ['your_package/src.cc'],
        include_dirs=[
            get_eigen_include()
        ],
        language='c++'
    )
]

setup(
...
    install_requires=['peigen>=0.0.9'],
    ext_modules=ext_modules,
...
)
```