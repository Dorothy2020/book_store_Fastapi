# book_store_Fastapi

Book Store API following CRUD Operation in FastAPI
This project is still in progress. Connecting it to the Postgres database. Along the way I am getting an error:
Error message: 
 conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (127.0.0.1), port 5432 failed: FATAL:  password authentication failed for user "postgres"
connection to server at "localhost" (127.0.0.1), port 5432 failed: FATAL:  password authentication failed for user "postgres"

(Background on this error at: https://sqlalche.me/e/20/e3q8)

