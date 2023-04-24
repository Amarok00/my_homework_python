#Instructions on how to install this assembly.
#Install docker on your device
#Go to the package folder
#docker run hello-world run the command to check the health
#docker build . -t app this is the command run the installation of the program
#docker run -p 8000:8000 -it app with this command, you will run the program on port 8000

FROM python:3.11.3-bullseye 

ENV PYTHONUBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install "poetry==1.4.2"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-ansi --only main

COPY my_app .

CMD ["uvicorn" ,"app:app" ,"--host" ,"0.0.0.0" ,"--port" ,"8000"]

EXPOSE 8000