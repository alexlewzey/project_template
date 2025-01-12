install:
	pip install uv
	rm -rf .venv/
	uv venv
	uv sync --all-extras

test:
	# static tests and formatting
	uv run pre-commit run --all-files
	# unit & integration tests
	uv run python -m pytest -sv --cov=src --cov-report=term-missing tests/

clean:
	rm -rf .venv tmp
