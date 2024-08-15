# About

This project was created to ease self-directed learning of foreign languages.
It relies on the premise that it is easier and more productive to learn
vocabulary and grammar if the subject matter is related to your interests and
every day experiences than otherwise uninteresting and uncommon material.

Record voice memos throughout your day of things you would like to be able to
say in another language and use this project to generate flashcards for study.

The currently supported languages are German, Italian, Spanish and
Swahili.


# Usage

Source the necessary bash environment variables:
```
source .bash_env
```

Start it up:
```
./run_dev.sh
```

Make migrations
```
./makemigrations.sh
```

Apply migrations
```
./migrate.sh
```

Run django test suite
```
./test.sh
```

Transcribe and translate audio file (wav and mp3 formats are supported)
```
python translate_audio.py [--fp <file-path>] [--base_url <base-url>]
```
NOTE: If you see a connection error, it is likely due to the backend having
tried to connect to the database before it was ready. This can be remedied by
restarting the backend container or by powering down the whole project and
starting it up again.

Power it down
```
./down.sh
```

# Helper commands

Start it up:
```
./run.sh
```
or

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

Start a new django app
```
./startapp.sh
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
