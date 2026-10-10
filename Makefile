.PHONY: sources check

# Validate sources/*.yaml and regenerate SOURCES.md.
sources:
	python3 tools/build_sources.py

# Validate, and fail if SOURCES.md is out of date.
check:
	python3 tools/build_sources.py --check
