FROM python:3.9

COPY server.py /app/server.py

WORKDIR /app

ENV CALC_PORT=8889

EXPOSE 8889

ENTRYPOINT ["python", "server.py"]