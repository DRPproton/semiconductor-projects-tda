# Environment setup

The project dependencies are listed in `requirements.txt`.

## Use the existing virtual environment

From the repository root:

```bash
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Create a new environment with `uv`

If `venv/` does not exist, create a `.venv` environment with `uv`:

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Register the Jupyter kernel

With the environment activated:

```bash
python -m ipykernel install --user \
  --name semiconductor-projects-tda \
  --display-name "Python (semiconductor-projects-tda)"
```

## Activate the environment later

For the existing environment:

```bash
source venv/bin/activate
```

For the `uv` environment:

```bash
source .venv/bin/activate
```

Leave the environment with:

```bash
deactivate
```

## VS Code notebook setup

1. Open **Python: Select Interpreter** from the Command Palette.
2. Select `venv/bin/python` or `.venv/bin/python`.
3. In the notebook, select the matching Python kernel.
