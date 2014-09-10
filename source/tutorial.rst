Tutorial
========


Prerequisites
-------------
Even though the package name is pysdmx, you should start by importing sdmx, the
name of the module.

.. code-block:: python

  >>> import sdmx

Statistical providers
---------------------

You can explore the capabilities of pysdmx by using introspection.

.. code-block:: python

  >>> sdmx.__all__
  ('ecb', 'ilo', 'fao', 'eurostat', 'Repository')

Repository is the main class, representing a data source. Each statistical
provider is an instance of that class.

.. code-block:: python

  >>> type(sdmx.eurostat)
  <class 'sdmx.Repository'>

As you can see, various statistical providers are implemented and can be used
out of the box. Alternatively, you can define your own repository. For example,
here is the implementation of eurostat in pysdmx:

.. code-block:: python

  >>> Repository('http://www.ec.europa.eu/eurostat/SDMX/diss-web/rest','2_1','ESTAT')

The first parameter is the URL of the webservice, the second parameter
is the version of SDMX used by the statistical provider and the third parameter
is the agencyID in SDMX lingo.

