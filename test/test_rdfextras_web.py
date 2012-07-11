import unittest

import threading 
import rdflib

import rdflib_sparqlstore

try: 
    import rdfextras_web.endpoint
except ImportError:
    from nose.exc import SkipTest
    raise SkipTest("rdfextras_web not installed.")

class TestSPARQL(unittest.TestCase): 
    def test(self): 
        g=rdflib.Graph()

        data="""<http://example.org/book/book1> <http://purl.org/dc/elements/1.1/title> "SPARQL Tutorial" .
<http://example.org/book/b\xc3\xb6\xc3\xb6k8> <http://purl.org/dc/elements/1.1/title> "Moose bite can be very n\xc3\xb6sty."@se .
 
"""

        g.parse(data=data, format='n3')

        # # create our own SPARQL endpoint

        app=rdfextras_web.endpoint.get(g)
        t=threading.Thread(target=lambda : app.run(port=57234))
        t.daemon=True
        t.start()
        import time
        time.sleep(1)
        store=rdflib_sparqlstore.SPARQLStore("http://localhost:57234/sparql", context_aware=False)
        g2=rdflib.Graph(store)
        b=rdflib.URIRef("http://example.org/book/book1")
        b2=rdflib.URIRef("http://example.org/book/b\xc3\xb6\xc3\xb6k8")
        DCtitle=rdflib.URIRef("http://purl.org/dc/elements/1.1/title")
        self.assertEqual(len(list(g2.triples((b,None,None)))), 1)
        self.assertEqual(list(g2.objects(b,DCtitle))[0], rdflib.Literal("SPARQL Tutorial"))

        self.assertEqual(list(g2.objects(b2,DCtitle))[0], list(g.objects(b2,DCtitle))[0])

    
