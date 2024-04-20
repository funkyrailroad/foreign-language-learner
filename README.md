# Instructions

Source the necessary bash environment variables:
```
source .bash_env
```

Start it up:
```
./run.sh
```
or
```
./run_dev.sh
```

Watch the logs
```
./logs.sh
```

Drop into a shell inside the backend container
```
./exec.sh
```

Psql into the database
```
./psql.sh
```

Power it down
```
./down.sh
```


# Get upstream changes

Set the new remote

```
git remote set-url origin <new_origin>
```

Set this repo as a parent to pull in upstream updates

```
git remote add parent git@github.com:funkyrailroad/django-starter-project.git
```
