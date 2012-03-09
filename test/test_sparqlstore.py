import unittest
import logging
try:
    import SPARQLWrapper
except ImportError:
    from nose.exc import SkipTest
    raise SkipTest("SPARQLWrapper not installed")

from rdflib import Graph, URIRef, Literal

_logger = logging.getLogger(__name__)

class SPARQLStoreDBPediaTestCase(unittest.TestCase):
    store_name = 'SPARQLStore'
    path = "http://dbpedia.org/sparql"
    storetest = True
    create = False

    def setUp(self):
        self.graph = Graph(store="SPARQLStore")
        self.graph.open(self.path, create=self.create)
        self.graph.store.baseURI = self.path
        ns = list(self.graph.namespaces())
        assert len(ns) > 0, ns

    def tearDown(self):
        self.graph.close()

    def test_Query(self):
        query = "select distinct ?Concept where {[] a ?Concept} LIMIT 1"
        res = self.graph.query(query, initNs={})
        for i in res.serialize(format="python"):
            assert type(i) == URIRef, i.n3()

    def test_initNs(self):
        query = """\
        SELECT ?label WHERE { ?s a xyzzy:Concept ; xyzzy:prefLabel ?label . } LIMIT 10
        """
        res = self.graph.query(query,
            initNs={"xyzzy":"http://www.w3.org/2004/02/skos/core#"})
        for i in res.serialize(format="python"):
            assert type(i) == Literal, i.n3()

    def test_noinitNs(self):
        query = """\
        SELECT ?label WHERE { ?s a xyzzy:Concept ; xyzzy:prefLabel ?label . } LIMIT 10
        """
        self.assertRaises(
                SPARQLWrapper.Wrapper.QueryBadFormed,
                self.graph.query,
                query)

    def test_query_with_added_prolog(self):
        prologue = """\
        PREFIX xyzzy: <http://www.w3.org/2004/02/skos/core#>
        """
        query = """\
        SELECT ?label WHERE { ?s a xyzzy:Concept ; xyzzy:prefLabel ?label . } LIMIT 10
        """
        res = self.graph.query(prologue+query)
        for i in res.serialize(format="python"):
            assert type(i) == Literal, i.n3()

from nose import SkipTest
import urllib2
try:
    assert len(urllib2.urlopen("http://dbpedia.org/sparql").read()) > 0
except:
    raise SkipTest("No HTTP connection.")

