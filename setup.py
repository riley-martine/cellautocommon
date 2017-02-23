"""Setup.py for cellautocommon."""

from setuptools import setup

setup(name="cellautocommon",
      version="0.1",
      description="Useful files/functions for cellular automata",
      url="http://github.com/mbmartine/cellautocommon",
      author="Riley Martine",
      author_email="riley.martine.0@gmail.com",
      license="MIT",
      packages=["cellautocommon"],
      install_requires=[
          "typing"
      ],
      zip_safe=False)
