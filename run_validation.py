"""Run explicit validation modes; never launches timing benchmarks."""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import io
import json
from pathlib import Path
import platform
import sys
from datetime import datetime, timezone
import unittest
import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("smoke", "edge", "full"), default="smoke")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    stream = io.StringIO()
    details = {}
    with contextlib.redirect_stdout(stream):
        if args.mode == "smoke":
            from validate_release_smoke import main as smoke
            smoke()
        elif args.mode == "edge":
            suite = unittest.defaultTestLoader.discover(str(Path(__file__).parent / "tests"))
            result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
            details = {"test_groups": result.testsRun, "failures": len(result.failures), "errors": len(result.errors)}
            if not result.wasSuccessful():
                raise RuntimeError(stream.getvalue())
        else:
            from propagation_path_dp_reference import validate_random
            from propagation_qubo_equivalence import validate as validate_qubo
            details = validate_random(seed=20261006, n_pairwise=200, n_directional=100, K=10)
            details["qubo_instances_passed"] = validate_qubo(seed=20261006, n=30)
    record = {"timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "mode": args.mode, "status": "PASS", "details": details,
              "python": sys.version, "numpy": np.__version__, "platform": platform.platform(),
              "stdout": stream.getvalue(),
              "note": "This is a new run record, not a recovered historical campaign log.",
              "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in Path(__file__).parent.glob("*.py")}}
    output = args.output or Path("validation_output") / f"{args.mode}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(stream.getvalue(), end="")
    print(f"Result record: {output}")

if __name__ == "__main__":
    main()
