"""CLI for semantic-boundary-enforcer."""
import sys
import argparse
from .enforcer import SemanticBoundaryEnforcer


def main():
    parser = argparse.ArgumentParser(description="Semantic Boundary Enforcer")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        enforcer = SemanticBoundaryEnforcer("Fix SQL query performance on users table", min_alignment_score=0.15)
        s1 = "Analyze query execution plan for users table"
        s2 = "Redesign color palette in CSS stylesheet"
        print(f"Step 1: {enforcer.evaluate_step(s1).to_dict()}")
        print(f"Step 2: {enforcer.evaluate_step(s2).to_dict()}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
