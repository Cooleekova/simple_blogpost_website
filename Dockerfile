# Please remember to rename django_heroku to your project directory name
FROM python:3-onbuild

# WORKDIR sets the working directory for docker instructions, please not use cd
WORKDIR /app

# sets the environment variable
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=blogpost_website.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3

EXPOSE 8000

# Install operating system dependencies.
RUN apt-get update -y && \
    apt-get install -y apt-transport-https rsync gettext libgettextpo-dev && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs &&\
    rm -rf /var/lib/apt/lists/*

# Install Gunicorn.
RUN pip install "gunicorn>=19.8,<19.9"

# start to install backend-end stuff
WORKDIR /app

# Install Python requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code.
COPY . .

# Run application
CMD gunicorn blogpost_website.wsgi:application





