import unittest
from rdflib.graph import Graph

class TestSPARQLStoreGraphCore(unittest.TestCase):

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

