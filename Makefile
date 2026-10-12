.PHONY: sources schedules check

# Validate sources/*.yaml and regenerate SOURCES.md.
sources:
	python3 tools/build_sources.py

# Check the numbers in the Articles and regenerate Schedules 1 and 2.
schedules:
	python3 tools/build_schedules.py

# Validate everything, fail if a generated file is out of date, and check links.
check:
	python3 tools/build_sources.py --check
	python3 tools/build_schedules.py --check
	python3 tools/check_links.py
