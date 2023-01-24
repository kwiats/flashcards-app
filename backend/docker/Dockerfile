FROM python:3.8


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /src

COPY requirements.txt /src/
RUN pip install -r requirements.txt --no-cache-dir

COPY . /src/
ADD ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
