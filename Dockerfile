FROM python:3.10-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install & use pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy
# --dev — Install both develop and default packages from Pipfile.
# --system — Use the system pip command rather than the one from your virtualenv.
# --deploy — Make sure the packages are properly locked in Pipfile.lock, and abort if the lock file is out-of-date.

# Create and switch to a new user and his workdir
#RUN useradd --create-home appuser
ADD . /app
WORKDIR /app
#USER appuser

# copy project files to workdir
COPY . .

# cd wordir to project dir
WORKDIR /app/data-analysis-app

# run kedro pipeline
CMD ["kedro", "run"]
