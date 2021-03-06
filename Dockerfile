FROM python:3.8.1

# Setting
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# Setup pipenv
RUN pip install -U pip && \
    pip install \
    pipenv \
    flake8 \
    yapf \
    flask \
    requests \
    gunicorn \
    pyppeteer \
    python-dotenv \
    pyotp \
    pandas && \
    curl https://cli-assets.heroku.com/install.sh | sh


WORKDIR /src

# Install dependencies
# COPY Pipfile Pipfile.lock ./
# RUN pipenv install --system --ignore-pipfile --deploy

# Copy source codes
COPY . .

# Image settings
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0:80"]
EXPOSE 80