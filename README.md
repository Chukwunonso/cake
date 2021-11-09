# CakeProject
This project was created using the excellent cookiecutter tool. A lot of the production-ready infrastructure was removed for this exercise (docker et al.)

```bash
pip install cookiecutter
cookiecutter https://github.com/tiangolo/full-stack-fastapi-postgresql
```

## Backend Requirements

* [Poetry](https://python-poetry.org/) for Python package and environment management.

## Backend local development

* Now you can open your browser and interact with these URLs:


Backend, JSON based web API based on OpenAPI: http://<domain_name>/api/

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://<domain_name>/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://<domain_name>/redoc


## General workflow (Local development)

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

From `./src/app/` you can install all the dependencies with:

```console
$ poetry install
```

Then you can start a shell session with the new environment with:

```console
$ poetry shell
```

Next, open your editor at `./app/` (instead of the project root: `./`), so that you see an `./app/` directory with your code inside. That way, your editor will be able to find all the imports, etc. Make sure your editor uses the environment you just created with Poetry.

Modify or add SQLAlchemy models in `./src/app/models/`, Pydantic schemas in `./src/app/schemas/`, API endpoints in `./src/app/api/`, CRUD (Create, Read, Update, Delete) utils in `./src/app/crud/`. 

### Backend tests

To test the backend run:

```console
$ DOMAIN=backend sh ./scripts/test.sh
```

The file `./scripts/test.sh` has the commands to generate a testing `docker-stack.yml` file, start the stack and test it.

The tests run with Pytest, modify and add tests to `./backend/app/app/tests/`.

If you use GitLab CI the tests will run automatically.

#### Local tests

Start the stack with this command:

```Bash
DOMAIN=backend sh ./scripts/test-local.sh
```
The `./backend/app` directory is mounted as a "host volume" inside the docker container (set in the file `docker-compose.dev.volumes.yml`).
You can rerun the test on live code:

```Bash
docker-compose exec backend /app/tests-start.sh
```

#### Test Coverage

Because the test scripts forward arguments to `pytest`, you can enable test coverage HTML report generation by passing `--cov-report=html`.

To run the local tests with coverage HTML reports:

```Bash
DOMAIN=backend sh ./scripts/test-local.sh --cov-report=html
```

To run the tests in a running stack with coverage HTML reports:

```bash
docker-compose exec backend bash /app/tests-start.sh --cov-report=html
```

### Migrations

Make sure you create a "revision" of your models and that you "upgrade" your database with that revision every time you change them. As this is what will update the tables in your database. Otherwise, your application will have errors.

* After changing a model (for example, adding a column), inside the container, create a revision, e.g.:

```console
$ alembic revision --autogenerate -m "Add column last_name to User model"
```

* Commit to the git repository the files generated in the alembic directory.

* After creating the revision, run the migration in the database (this is what will actually change the database):

```console
$ alembic upgrade head
```
