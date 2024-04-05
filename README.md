# Instructions

Enter correct database credentials and rename them
```
./mysite/pgpass -> ./mysite/.pgpass
./mysite/pg_service.conf -> ./mysite/.pg_service.conf
```

Start it up:
```
docker compose up -d
```

Watch the logs
```
docker compose logs -f
```
