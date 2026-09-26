# Development Notes

## Setup

The app uses Python 3 and Flask. In this workspace, Flask is installed in `.venv`.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install Flask
```

## Run

```sh
python app.py
```

Open `http://localhost:5000`. The interface is server-rendered HTML and CSS; calculator keys submit regular forms and do not rely on JavaScript.

## Verify

```sh
python -m unittest -v
```

The expression evaluator uses Python's AST only to parse a restricted set of arithmetic operators, approved functions, and constants. It does not evaluate arbitrary Python code.