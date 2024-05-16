# Data Science Project Template

This is a template repo for data science project.

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
|- ruff.toml         # ruff config file
|- pdm.lock          # pdm lock file
|- README.md         # readme file
|- .pre-commit-config.yaml         # pre-commit config file
```

## Getting Started 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


## Prerequisites

- `pdm`: python packaging and dependency management tool, [installation](https://github.com/pdm-project/pdm?tab=readme-ov-file#installation)

## Create environement

Add packages to the `dependencies` or `[tool.pdm.dev-dependencies]` in `pyproject.toml`. Then run bellow command to install all packages.

```
make init
```

Install 

```
pre-commit install --hook-type commit-msg
```

## Usage

A recommended commit workflow.

```
make lint  # check the code quality
make format  # fix errors and check the code quality
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
pdm publish  # build and publish on the pypi
git tag v0.0.1  # create tag
git push origin v0.0.1  # push tag to github
```


### Code Quality

```
make lint
```

This will run ruff (replace isort, flake8), codespell to check the code.

```
make format
```

This will run ruff (replace black) to format the code.

```
make mypy
```

This will run mypy to chekc the type of code.


### Test

Run bellow command will test the code.

```
make test
```


### Commit Message Checker

We use `pre-commit` hook to check the commit message. When you commit a message, it will check whether the message follow below format.

```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: Optional, can be anything specifying the scope of the commit change.
  |                          For example $location|$browser|$compile|$rootScope|ngHref|ngClick|ngView, etc.
  |                          In App Development, scope can be a page, a module or a component.
  │
  └─⫸ Commit Type: feat|fix|docs|style|refactor|test|chore|perf|ci|build|temp
```


type meanings: https://github.com/legend80s/commit-msg-linter
```
  correct format: <type>[scope]: <subject>
  example: docs: update README to add developer tips

  type:
    feat     A new feature.
    fix      A bug fix.
    docs     Documentation only changes.
    style    Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
    refactor A code change that neither fixes a bug nor adds a feature.
    test     Adding missing tests or correcting existing ones.
    chore    Changes to the build process or auxiliary tools and libraries such as documentation generation.
    perf     A code change that improves performance.
    ci       Changes to your CI configuration files and scripts.
    build    Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm).
    temp     Temporary commit that won't be included in your CHANGELOG.
```

You can specify the commit message format by change the regex enty in `.pre-commit-config.yaml`. 
