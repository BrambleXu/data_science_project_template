# Data Science Project Template (WIP)

Write about 1-2 paragraphs describing the purpose of your project.

## Project structure

```
Project_folder/
|- .github/          # GitHub workflows
|- .vscode/          # vscode configs. You can delete it if you are using other editor
|- data/             # dataset. Usually ignored due to the size
|- docs/             # documents
|- examples/         # script examples for demo
|- notebooks/        # notebooks for demo
|- outputs/          # store trained models, predict results, etc.
|- src/              # source code
|- tests/            # Test files should mirror the src folder
|- .gitignore        # ignore folder or files
|- LICENSE           # LICENSE
|- Makefile          # simplify command
|- pyproject.toml    # project config file
|- README.md         # readme file
```

## Getting Started 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


## Prerequisites

- `conda`: python environement management tool
- `poetry`: python packaging and dependency management tool


## Create environement

Setup your environement and install project dependencies
```
conda create -n my_project python=3.8
conda activate my_project
```

Add packages to the `[tool.poetry.dependencies]` or `[tool.poetry.dev-dependencies]` in `pyproject.toml`. Then run bellow command to install all packages.

```
make init
```

## TL;DR

A recommended commit workflow:

```
make lint  # check the code quality and fix errors
make test  # test code functionality and fix bugs
git add xxx  # add changes to stage
git commit -m "feat: "  # commit changes. The commit message should follow bellow convention
git push origin main  # push changes. Change 'main' to your branch
```

[Semantic Commit Messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

- feat: new feature for the user, not a new feature for build script
- fix: bug fix for the user, not a fix to a build script
- docs: changes to the documentation
- style: formatting, missing semi colons, etc; no production code change
- refactor: refactoring production code, eg. renaming a variable
- test: adding missing tests, refactoring tests; no production code change
- chore: updating grunt tasks etc; no production code change


A recommended realse workflow:

If you need to update your package, simply increment the version in the pyproject.toml file and use poetry publish (after you build the new package with poetry build).

```
# increment the version in the pyproject.toml, here we assume the version is 0.0.1
poetry build  # build the release files
poetry publish # publish on the pypi
git tag v0.0.1  # create tag
git push origin v0.0.1  # push tag to github
```


### Code Quality

```
make lint
```

This will run black, isort, ruff, mypy, codespell to check the code.


### Test

Run bellow command will test the code.

```
make test
```


### TODO

- CI workflow ruff
- 