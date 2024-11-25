FROM python:3.11.10-bookworm

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install -r /app/requirements.txt

COPY ./ /app

CMD [ "sh", "-c", "export PYTHONPATH=$PYTHONPATH:$PWD && python src/main.py" ]
