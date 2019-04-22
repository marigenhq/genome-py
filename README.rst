genome reader
=============
.. image:: https://travis-ci.org/marigenhq/genome-reader.svg?branch=master
  :target: https://travis-ci.org/marigenhq/genome-reader
  :alt: Build Status
     
.. image:: https://codecov.io/gh/marigenhq/genome-reader/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/marigenhq/genome-reader
  :alt: codecov

.. image:: https://badge.fury.io/py/genome-reader.svg
  :target: https://badge.fury.io/py/genome-reader
  :alt: Pypi Version
  
.. image:: https://readthedocs.org/projects/genome-reader/badge/?version=latest
  :target: https://genome-reader.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status


Installing
==========

.. code-block:: shell

    pip install genome-reader

Usage
=====

.. code-block:: python
   :linenos:

    from genome_reader import load
    genome = load('path/to/genome/data')
    # <Genome: SNPs=553190, name='data'>


Development
===========

`Data source`_

.. _Data source: https://my.pgp-hms.org/public_genetic_data?utf8=%E2%9C%93&data_type=23andMe&commit=Search

