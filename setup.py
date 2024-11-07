from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        "glmath._cosmomath",
        sources=[
            "ext_src/_cosmomath.pyx"
        ],
        include_dirs=["ext_src", numpy.get_include()],
        language="c++"
    )
]


setup(ext_modules=cythonize(extensions))
