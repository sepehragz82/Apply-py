# Apply-py

## 1: Requirements

- Python
- Pip

## 2: Installation

```bash
pip install fastapi
pip install sqlalchemy
pip install passlib[bcrypt]
pip install python-jose[cryptography]
pip install pydantic-settings
pip install mysql-connector-python
```

## 3: Configuration

Edit `.env` file
Set `DATABASE_URL` field

## 4: Execution

```bash
uvicorn src.main:app
```
