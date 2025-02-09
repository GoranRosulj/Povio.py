# Povio.py

repos:
  - repo: https://github.com/pre-commit/mirrors-black
    rev: v21.9b0  # Use the latest version
    hooks:
      - id: black

  - repo: https://github.com/pre-commit/mirrors-flake8
    rev: v3.9.2  # Use the latest version
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.4.0  # Use the latest version
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
