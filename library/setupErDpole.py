#!/usr/bin/env python

"""
This file belong to https://github.com/snolfi/evorobotpy
Author: Stefano Nolfi, stefano.nolfi@istc.cnr.it

setupErDpole.py, python wrapper for dpole.cpp

This file is part of the python module ErDpole.so that include the following files:
dpole.cpp, dpole.h, utilities.cpp, utilities.h, ErDpole.pxd, ErDpole.pyx and setupErDpole.py
And can be compiled with cython and installed with the commands: cd ./evorobotpy/lib; python3 setupErDpole.py build_ext –inplace; cp ErDpole*.so ../bin
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy

# linux
include_gsl_dir = "/usr/include/gsl"
lib_gsl_dir = "/usr/lib/x86_64-linux-gnu"

setup(
    cmdclass={"build_ext": build_ext},
    ext_modules=[
        Extension(
            "ErDpole",
            sources=["ErDpole.pyx"],
            language="c++",
            include_dirs=[numpy.get_include(), include_gsl_dir],
            libraries=["gsl", "gslcblas"],
            library_dirs=[lib_gsl_dir],
        )
    ],
)
