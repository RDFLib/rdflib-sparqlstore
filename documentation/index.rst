.. SPARQLStore RDFLib Store documentation

|today|

==============================================================
SPARQLStore :: a read-only Store for wrapping SPARQL endpoints
==============================================================

Contents:
=========
.. toctree::
   :maxdepth: 2

Introduction
============

This is a read-only RDFLib Store around Ivan Herman et al.'s SPARQL service
wrapper.

This version works with vanilla SPARQLWrapper installed by ``easy_install``
or similar.


Example
=======

>>> from rdflib import Graph, URIRef
>>> 
>>> graph = Graph(store="SPARQLStore")
>>> graph.open("http://dbpedia.org/sparql")
>>> 
>>> ns = list(graph.namespaces())
>>> assert len(ns) > 0, ns
>>> 
>>> query = "select distinct ?Concept where { [] a ?Concept } LIMIT 1"
>>> 
>>> for i in graph.query(query):
...     assert type(i[0]) == URIRef, i[0].n3()
... 
>>> 


Module API
++++++++++

.. currentmodule:: rdflib_sparqlstore.sparqlstore

:mod:`~rdflib_sparqlstore.sparqlstore`
----------------------------------------
.. automodule:: rdflib_sparqlstore.sparqlstore
.. autoclass:: SPARQLStore
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

