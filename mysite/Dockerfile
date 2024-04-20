FROM python:3

RUN apt update -y
RUN apt install -y nodejs

RUN useradd -ms /bin/bash appuser
USER appuser

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ENV PATH="${PATH}:~/.local/bin"

COPY . /app
WORKDIR /app

ENTRYPOINT ["bash", "entrypoint.sh"]
