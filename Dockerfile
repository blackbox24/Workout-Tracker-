FROM python:3.12-alpine AS builder

WORKDIR /app

RUN apt update &&
    apk add --no-cache gcc \ 
    musl-dev \
    libffi-dev

COPY ./requirements.txt ./pyproject.toml ./

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.12-alpine

WORKDIR /app

RUN addgroup -S myuser && adduser -S myuser -G myuser

COPY --from=builder /install /usr/local
COPY --chown=myuser:myuser . .

USER myuser

EXPOSE 9000


CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:9000"]