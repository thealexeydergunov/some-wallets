FROM python:3.11.4

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apt-get update && apt-get install -y netcat python-dev python3-dev libevent-dev
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /usr/src/app
EXPOSE 8000
#RUN /usr/src/app/manage.py collectstatic
#ENTRYPOINT ["/usr/src/app/entrypoint-backend.sh"]

CMD ["python", "-m", "uvicorn", "wallets.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
