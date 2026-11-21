import unittest
from engine import assess
class EngineTests(unittest.TestCase):
    def test_matching(self):
        self.assertEqual(assess({"x":3},[{"field":"x","op":"gt","value":2,"severity":"high","message":"test"}])["count"],1)
    def test_missing(self):
        self.assertEqual(assess({},[{"field":"x","op":"eq","value":False,"severity":"high","message":"test"}])["count"],0)
    def test_type_safety(self):
        self.assertEqual(assess({"x":True},[{"field":"x","op":"gt","value":0,"severity":"high","message":"test"}])["count"],0)
    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            assess({"x":3},[{"field":"x","op":"bad","value":2,"severity":"high","message":"test"}])
