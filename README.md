# Payment Project

### This is simple payment api using fast-api.

# How to Install

### Create a virtual environment:

`python3 -m venv env`

### Activate the virtual environment:

`source env/bin/activate`

### Install requirements:

`pip3 install -r requirements.txt`

### Create an environment file in the core folder named .env and put the informations:

```
touch .env
```

```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Run the server:

`uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`

## Run using docker :

`docker compose up --build -d`



## To test on postman :
### import the postman collection from [Payment Api.postman_collection.json](https://github.com/abdullah-algumar/PaymentSystemFastApi/Payment Api.postman_collection.json) file and test the endpoints.


## Run Test file:

`python tests/test.py`

### Note: You can find the APIs Docs on this url : `base_url/docs` and `base_url/redoc`