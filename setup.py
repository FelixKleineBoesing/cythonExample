from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy as np


REQUIRES = ['numpy', ]

PACKAGE_DIR = "cythonexample"
PACKAGES = [PACKAGE_DIR]

ext_1 = Extension(PACKAGE_DIR + ".wrapped",
                  [PACKAGE_DIR + "/lib/cfunc.c", PACKAGE_DIR + "/wrapped.pyx"],
                  libraries=[],
                  include_dirs=[np.get_include()])


EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name="cythonexample",
          version="0.0.1",
          description="Cython example",
          author="Felix Kleine Bösing",
          author_email="felix.boesing@dummy.de",
          license="Apache 2.0",
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
          )