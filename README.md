# CakeProject
This project was created using the excellent cookiecutter tool. A lot of the production-ready infrastructure was removed for this exercise (docker et al.)

```bash
pip install cookiecutter
cookiecutter https://github.com/tiangolo/full-stack-fastapi-postgresql
```

## Set up (Development and Deployment)
* [AWS Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) set up with security group set to public for development. Take note of the VPC, Security Groups and Subnets
* Populate `src/app/.env_example` and copy over as `src/app/.env` with the credentials 
* Create a virtual env at _src/app_ `python3 -m .venv cake-env` and then `source .venv/bin/activate`
* Run database migrations in the `src/` directory
```console
$ alembic upgrade head
```
* Install [serverless](https://serverless.com) with `npm install -g severless` 
* Configure with `serverless config credentials --provider aws --key <YOUR_KEY> --secret <YOUR_SECRET_KEY>`. If you have configured _aws cli_, this won't be necessary.
* In `app/` directory run `npm install`. 
* Time to deploy run `sls deploy`


## Issues:

* I have unfortunately run into issues with deploying using serverless. I am getting timeout errors from lambda function while doing anything that touches the database from the lambda endpoint.


### What I have done:
- Mapped the Security Groups and Subnet of the VPC to the Function in serverless.yml

### What I suspect the problem to be:
- Need to allow the lambda function access to the internet using a NAT Gateway (credit StackOverflow)

### My workaround:
To at least demonstrate the application in action, I have fired up the app locally and piped it to the internet using [ngrok](https://ngrok.com).
It is available here.

### Long term solution:
Explore examples available at https://github.com/serverless/examples for inspiration to set up a pain-free architecture.

## Live Endpoints
## <domain_main>
- AWS: https://g1xc5zdtj3.execute-api.eu-west-2.amazonaws.com/dev/
- Ngrok: http://0678-92-26-30-245.ngrok.io/docs

JSON based web API based on OpenAPI: http://<domain_name>/api/
Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://<domain_name>/docs
Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://<domain_name>/redoc


## Local development

Open your editor at `./app/` (instead of the project root: `./`), so that you see an `./app/` directory with your code inside. That way, your editor will be able to find all the imports, etc. Make sure your editor uses the environment you just created.

Modify or add SQLAlchemy models in `./src/app/models/`, Pydantic schemas in `./src/app/schemas/`, API endpoints in `./src/app/api/`, CRUD (Create, Read, Update, Delete) utils in `./src/app/crud/`. 

```console
$ alembic revision --autogenerate -m "Add column last_name to User model"
```

Always commit to the git repository the files generated in the alembic directory.
