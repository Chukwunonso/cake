# CakeProject
This project was created using the excellent cookiecutter tool. A lot of the production-ready infrastructure was removed for this exercise (docker et al.)

```bash
pip install cookiecutter
cookiecutter https://github.com/tiangolo/full-stack-fastapi-postgresql
```
## Prerequisites
* [AWS Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) set up with security group set to public for development. Take note of the VPC, Security Groups and Subnets
* Populate app/.env with the credentials 
* Populate [serverless configuration](./src/app/serverless.yaml) with VPC Security Group and Subnets. See []

Backend, JSON based web API based on OpenAPI: http://<domain_name>/api/

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://<domain_name>/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://<domain_name>/redoc


## General workflow (Local development)

Next, open your editor at `./app/` (instead of the project root: `./`), so that you see an `./app/` directory with your code inside. That way, your editor will be able to find all the imports, etc. Make sure your editor uses the environment you just created with Poetry.

Modify or add SQLAlchemy models in `./src/app/models/`, Pydantic schemas in `./src/app/schemas/`, API endpoints in `./src/app/api/`, CRUD (Create, Read, Update, Delete) utils in `./src/app/crud/`. 


```console
$ alembic revision --autogenerate -m "Add column last_name to User model"
```

* Commit to the git repository the files generated in the alembic directory.

* After creating the revision, run the migration in the database (this is what will actually change the database):

```console
$ alembic upgrade head
```
