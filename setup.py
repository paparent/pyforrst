import os
from distutils.core import setup

from pyforrst import __version__

setup(name='pyforrst',
      version=__version__,
      author='PA Parent',
      author_email='paparent@paparent.me',
      description='Python interface to Forrst API',
      long_description=file(
          os.path.join(
              os.path.dirname(__file__),
              'README'
            )
      ).read(),
      license="MIT",
      url="http://github.com/paparent/pyforrst",
      py_modules=['pyforrst'],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Programming Language :: Python",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: MIT License",
      ],
     )
