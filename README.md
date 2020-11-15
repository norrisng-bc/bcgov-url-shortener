# django-react-boilerplate
A minimalist boilerplate for Django with React.

### Setup

Create a .env file that stores database and redis configurations like below:

```
POSTGRES_DB=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
REDIS_HOST=redis
```

### Then build containers:

```
$ docker-compose build --no-cache
```

Now you are ready to start the development.

```
$ docker-compose up -d
```
**Note:** Backend app runs at **8000** port and frontend app runs at **8080** port.