from distutils.core import setup

long_description = open('README').read()

setup(name="python-wmata",
      version='0.1',
      py_modules=["pywmata"],
      description="Library for interacting with the WMATA Metro Transparent Data Sets API",
      author="Aaron Bycoffe",
      author_email = "bycoffe@gmail.com",
      license='BSD',
      url="http://github.com/bycoffe/python-wmata",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
      )
