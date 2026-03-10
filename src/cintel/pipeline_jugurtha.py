"""
pipeline_jugurtha.py - Project script (example).

Author: Jugurtha Kacimi
Date: 2026-03-10

Purpose:
  Confirm your project environment is set up correctly.
  Run this script to see a log message in the terminal.

Run as a Module:
  uv run python -m cintel.pipeline_case
"""

# === DECLARE IMPORTS ===

# First from the Python standard library (no installation needed)
import logging
import time
from pathlib import Path

# Then, external dependencies (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header, log_path

# Capture start time of the script for logging purposes
START_TIME: float = time.time()

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P1", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===

ROOT_DIR: Path = Path.cwd()
DOCS_DIR: Path = ROOT_DIR / "docs"

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DOCS_DIR", DOCS_DIR)

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")

    # Log the total execution time of the script
    elapsed_time: float = time.time() - START_TIME
    LOG.info("Total execution time: %.2f seconds", elapsed_time)


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
