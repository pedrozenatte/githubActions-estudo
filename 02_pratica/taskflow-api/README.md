# Taskflow API

Taskflow API e um projeto basico em Python com FastAPI para servir como base de estudos de GitHub Actions, CI e CD.

O objetivo nao e criar uma API complexa, mas manter uma estrutura realista para praticar automacoes como testes, coverage, lint, formatacao, build de imagem Docker e deploy.

## Estrutura

```text
taskflow-api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── repository.py
│   └── services.py
├── tests/
│   ├── test_health.py
│   ├── test_tasks_unit.py
│   └── test_tasks_api.py
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── README.md
└── .gitignore
```

## Endpoints

- `GET /health`
- `GET /tasks`
- `POST /tasks`
- `GET /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

As tarefas ficam em memoria e possuem os campos:

- `id`
- `title`
- `done`

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Rodar a API localmente

```bash
uvicorn app.main:app --reload
```

A API ficara disponivel em:

```text
http://127.0.0.1:8000
```

A documentacao interativa do FastAPI ficara em:

```text
http://127.0.0.1:8000/docs
```

## Rodar os testes

```bash
pytest
```

## Rodar coverage

```bash
pytest --cov=app
```

A meta minima configurada e de 80%.

## Rodar lint

```bash
ruff check .
```

## Verificar formatacao

```bash
black --check .
```

Para formatar o codigo:

```bash
black .
```

## Rodar com Docker

Crie a imagem:

```bash
docker build -t taskflow-api .
```

Rode o container:

```bash
docker run --rm -p 8000:8000 taskflow-api
```

Depois acesse:

```text
http://127.0.0.1:8000/docs
```

## CI/CD

Este projeto foi criado para servir como ambiente de aprendizado de GitHub Actions e CI/CD.

Os arquivos de workflow nao foram criados de proposito, para que voce possa implementar manualmente os pipelines depois.
