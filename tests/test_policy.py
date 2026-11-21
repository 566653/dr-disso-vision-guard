import tempfile
import unittest
from pathlib import Path
from policy import validate_rules, summarize, export_report

class PolicyTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(len(validate_rules([{"field":"x","op":"gt","value":2,"severity":"high","message":"test"}])),1)
    def test_bad_operator(self):
        with self.assertRaises(ValueError):
            validate_rules([{"field":"x","op":"exec","value":2,"severity":"high","message":"test"}])
    def test_invalid_threshold(self):
        with self.assertRaises(ValueError):
            validate_rules([{"field":"x","op":"gt","value":"2","severity":"high","message":"test"}])
    def test_summary(self):
        self.assertTrue(summarize({"alerts":[{"severity":"critical"}]})["requires_review"])
    def test_report(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(export_report({"alerts":[]},Path(temp)/"report.json")["schema_version"],2)
