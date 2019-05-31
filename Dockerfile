FROM python

RUN mkdir /app
COPY src /app/src
COPY calculate_cli.py /app
COPY __init__.py /app

RUN mkdir /data

WORKDIR /app

#ENTRYPOINT [ "python", "./calculate_cli.py" ]