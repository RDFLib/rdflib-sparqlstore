This is an RDFLib store around Ivan Herman et al.'s SPARQL service wrapper.

This extension has revived support for namespace bindings.

```
import rdflib
g=rdflib.ConjunctiveGraph('SPARQLStore')
g.open("http://dbpedia.org/sparql")
...
```

a SPARQLUpdateStore is also available: 

```
import rdflib
g=rdflib.ConjunctiveGraph('SPARQLUpdateStore')
g.open("http://localhost:3030/dataset/sparql", "http://localhost:3030/dataset/update")
...
```

If you create the store object explicitly and set context_aware to False, you can also use rdflib.Graph: 

```
import rdflib
import rdflib_sparqlstore

store=rdflib_sparqlstore.SPARQLStore("http://dbpedia.org/sparql", context_aware=False)
g=rdflib.Graph(store)
```

[![Build Status](https://travis-ci.org/RDFLib/rdflib-sparqlstore.png?branch=master)](https://travis-ci.org/RDFLib/rdflib-sparqlstore)
