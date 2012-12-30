
RDFLib SPARQLstore
==================

This is an RDFLib extension that provides an RDFLib Store around Ivan Herman
et al.'s [SPARQL service wrapper](http://pypi.python.org/pypi/SPARQLWrapper).

In essence, it allows a SPARQL 1.0 endpoint to behave as if it were a read-only
RDFLib Store.

The extension also provides a read/write SPARQLUpdateStore, for use when the SPARQL
endpoint supports SPARQL 1.1 update operations.

This extension has revived support for namespace bindings.


Install with:

    $ pip install rdflib_sparqlstore

Basic usage is

1. instantiate an RDFLib ConjunctiveGraph with "SPARQLStore" as the first
   positional arg and then

2. ``open``ing a known SPARQL endpoint

e.g.

    import rdflib
    g = rdflib.ConjunctiveGraph('SPARQLStore')
    g.open("http://dbpedia.org/sparql")


A SPARQLUpdateStore is also available, the example below shows how a graph of 
updates can be applied to an existing endpoint / store:

    import rdflib
    g = rdflib.ConjunctiveGraph('SPARQLUpdateStore')
    g.open("http://localhost:3030/dataset/sparql",
           "http://localhost:3030/dataset/update")


If the store object is explicitly created with the ``context_aware`` keyword
param set to ``False``, then rdflib.Graph can be used: 

    import rdflib
    import rdflib_sparqlstore

    store = rdflib_sparqlstore.SPARQLStore("http://dbpedia.org/sparql",
                                           context_aware=False)
    g =  rdflib.Graph(store)


[![Build Status](https://travis-ci.org/RDFLib/rdflib-sparqlstore.png?branch=master)](https://travis-ci.org/RDFLib/rdflib-sparqlstore)
