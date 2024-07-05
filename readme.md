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

### For sqlite

Set `DATABASE_URL` to `"sqlite:///./apply.db"`

### For mysql

Set `DATABASE_URL` to `"mysql+mysqlconnector://root:password@localhost/apply"`

`password` is your mysql root password.

Also, you should create a database (schema) and name it `apply`.

## 4: Execution

```bash
uvicorn src.main:app
```
