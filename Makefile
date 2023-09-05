init:
	poetry install

lint:
	poetry run black src	
	poetry run black examples
	poetry run black tests

	poetry run isort src
	poetry run isort examples
	poetry run isort tests

	poetry run ruff src
	poetry run ruff examples
	poetry run ruff tests

	poetry run codespell src
	poetry run codespell examples
	poetry run codespell tests

test:
	poetry run pytest tests
