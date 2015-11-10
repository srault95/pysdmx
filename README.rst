======
pysdmx
======

Python interface to SDMX

|Build Status| |Build Doc| |Coveralls|

Installation
------------

For the time being, pysdmx is not on pypi. You can use the standard procedure from distutils.

    python3 setup.py install

Usage
-----

pysdmx provides a bookmark for the SDMX endpoint provided by Eurostat. You can easily retrieve a pandas.DataFrame()

::

    >>>import pysdmx
    >>>pysdmx.eurostat.dataframe('cdh_e_fos','..PC.FOS1.BE','2005','2011')

    
.. |Build Status| image:: https://travis-ci.org/Widukind/pysdmx.svg?branch=master
   :target: https://travis-ci.org/Widukind/pysdmx
   :alt: Travis Build Status
   
.. |Build Doc| image:: https://readthedocs.org/projects/widukind/badge/?version=latest
   :target: http://widukind-pysdmx.readthedocs.org/en/latest/?badge=latest
   :alt: Documentation Status   
   
.. |Coveralls| image:: https://coveralls.io/repos/Widukind/pysdmx/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/Widukind/pysdmx?branch=master
   :alt: Coverage   
    
