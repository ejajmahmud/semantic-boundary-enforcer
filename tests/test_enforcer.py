"""Tests for semantic-boundary-enforcer."""
import unittest
from semantic_boundary_enforcer.enforcer import SemanticBoundaryEnforcer


class TestBoundaryEnforcer(unittest.TestCase):
    def setUp(self):
        self.enf = SemanticBoundaryEnforcer("Migrate auth tokens to JWT", min_alignment_score=0.15)

    def test_aligned_step(self):
        res = self.enf.evaluate_step("Generate JWT signing key and update auth tokens")
        self.assertTrue(res.aligned)

    def test_divergent_step(self):
        res = self.enf.evaluate_step("Download MP3 sound effects for game UI")
        self.assertFalse(res.aligned)
