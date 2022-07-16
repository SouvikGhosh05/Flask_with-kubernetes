FROM python:3.9.6

COPY .  /app
WORKDIR /app
RUN pip install -U pip Flask requests
ENV FLASK_ENV development
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
