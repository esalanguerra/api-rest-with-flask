# API Rest Com Flask

Este é um repositório de primeira api rest com o framework python flask. com objetivo de fazer um crud básico com sqlite.

## Iniciando Api

```sh
python -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

flask run
```

## Endpoints `http://localhost:5000/api/v1`

```py
  GET /books
  GET /books/:id
  POST /books
  PATCH /books/:id
  DELETE /books/:id
```
