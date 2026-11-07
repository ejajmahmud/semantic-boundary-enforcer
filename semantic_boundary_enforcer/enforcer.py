"""Core Semantic Boundary Enforcer implementation."""
import re
import math
from typing import Set, Dict, Any, List


class AlignmentScore:
    def __init__(self, score: float, aligned: bool, reason: str):
        self.score = score
        self.aligned = aligned
        self.reason = reason

    def to_dict(self) -> Dict[str, Any]:
        return {
            "alignment_score": round(self.score, 3),
            "is_aligned": self.aligned,
            "reason": self.reason
        }


class SemanticBoundaryEnforcer:
    def __init__(self, root_goal: str, min_alignment_score: float = 0.25):
        self.root_goal = root_goal
        self.min_alignment_score = min_alignment_score
        self._goal_tokens = self._tokenize(root_goal)

    def _tokenize(self, text: str) -> Set[str]:
        words = re.findall(r"\w+", text.lower())
        # Filter basic stop words
        stops = {"the", "a", "an", "in", "on", "of", "to", "for", "with", "and", "is"}
        return set(w for w in words if w not in stops)

    def evaluate_step(self, step_action_desc: str) -> AlignmentScore:
        step_tokens = self._tokenize(step_action_desc)
        if not step_tokens or not self._goal_tokens:
            return AlignmentScore(1.0, True, "Empty baseline or step")

        intersection = len(self._goal_tokens.intersection(step_tokens))
        union = len(self._goal_tokens.union(step_tokens))
        score = intersection / union if union > 0 else 0.0

        is_aligned = score >= self.min_alignment_score
        reason = "Step within semantic boundary" if is_aligned else f"Step diverged from goal (score {score:.2f} < {self.min_alignment_score})"

        return AlignmentScore(score, is_aligned, reason)
