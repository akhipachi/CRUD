used fastapi for api, sqlite for database, sqlalchemy for sql haldling
used docker for containerizing
docker commandes:
docker build --tag app .
docker run --publish 8080:8080 --detach --name app app

use /docs for apidocs