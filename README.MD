# Item Management APIs

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.14+-red.svg)](https://www.django-rest-framework.org/)
[![uv](https://img.shields.io/badge/uv-powered-blue.svg)](https://github.com/astral-sh/uv)
[![Python](https://img.shields.io/badge/Python-3.10-yellow.svg)](https://www.python.org/)

A Django REST Framework APIs for item management with CRUD operations, powered by **uv** - the ultra-fast Python package manager.

## 🌟 Features

- Complete CRUD operations for item management
- Function-based views for simplicity and performances
- Filtering capabilities (by ID, name, date components)
- Powered by uv for dependency and environment management
- Python 3.10 isolated environment (no global installation needed)

## 📋 Prerequisites

- Windows 10/11 or higher
- Python 3.12 installed globally (for uv itself)
- uv package manager installed
- No need to install Python 3.10 system-wide—uv will fetch it for you!

## 🚀 Quick Setup

### 1. Install uv (if not already)

```bash
pip install uv
```
*Or use the standalone installer from the [uv docs](https://github.com/astral-sh/uv).*

### 2. Create a Python 3.10 virtual environment

```bash
uv venv --python 3.10 env_ItemApp
```

### 3. Activate the virtual environment

```bash
.\env_ItemApp\Scripts\activate
```

### 4. Initialize project structure

```bash
uv init
```

### 5. Install core dependencies

```bash
uv add django djangorestframework django-filter pylint
```

### 6. Sync your environment to the lockfile

```bash
uv sync
```

### 7. Export requirements.txt (for compatibility)

```bash
uv export --format=requirements-txt > requirements.txt
```

### 8. Generate Pylint configuration

```bash
pylint --generate-rcfile > .pylintrc
```

### 9. Start Django project and app

```bash
django-admin startproject ItemManagementSystem .
python manage.py startapp items
```

## 📁 Project Structure

```
.
├── .python-version        # Pinned Python 3.10 version
├── .pylintrc              # Pylint configuration
├── env_ItemApp/           # uv-managed venv with Python 3.10
├── ItemManagementSystem/  # Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── items/                 # Django app for items
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── pyproject.toml         # Project metadata & dependencies
├── uv.lock                # Locked dependency graph
└── requirements.txt       # Exported requirements
```

## 🔌 API Endpoints

| URL | Method | Description |
|-----|--------|-------------|
| `/items/` | GET | List all items or filter by itemID/day/month/year/itemName |
| `/items/` | POST | Create a new item |
| `/items/<itemID>/` | GET | Retrieve a single item by itemID |
| `/items/<itemID>/` | PUT | Update an item by itemID |
| `/items/<itemID>/` | DELETE | Delete an item by itemID |

## 🧹 Linting

Run Pylint on your items app to catch errors & style issues:

```bash
uv run pylint items --errors-only
```

## 📦 Dependencies

All runtime dependencies are locked in `uv.lock` and mirrored in `requirements.txt` for compatibility.

Install them via:

```bash
uv sync            # preferred (uses uv.lock)
# or
uv pip install -r requirements.txt
```

## 📚 UV Commands Reference

| Command | Description |
|---------|-------------|
| `uv python list --all-versions` | List all Python versions uv can install |
| `uv python install 3.10` | Download & install Python 3.10 |
| `uv venv --python 3.10 env_ItemApp` | Create a venv named env_ItemApp with Python 3.10 |
| `uv init` | Scaffold a new project (pyproject.toml, .venv, etc.) |
| `uv add <pkg>` | Add dependencies (e.g. django, djangorestframework) |
| `uv remove <pkg>` | Remove a dependency |
| `uv sync` | Sync installed packages to match uv.lock |
| `uv lock` | Generate/update uv.lock |
| `uv export --format=requirements-txt` | Export uv.lock to requirements.txt |
| `uv pip compile pyproject.toml -o requirements.txt` | Lock dependencies into a requirements file |
| `uv run django-admin startproject …` | Run Django commands reproducibly in the venv |
| `uv tree` | View dependency tree |
| `uv build` | Build sdist & wheel archives |
| `uv publish --index pypi` | Publish your package to PyPI |
| `uv --help / uv <cmd> --help` | Show help messages |

## 📄 License

MIT

---

Happy coding with uv and Django REST Framework! 🎉