# Base image using Python 3.12 on Debian Bullseye (slim variant for smaller image size)
FROM python:3.12-slim-bullseye AS development

# Set environment variables for Python and Poetry:
# Ensure Python runs in unbuffered mode and doesn't write .pyc files to disc
# Disable pip's cache and version check for faster installs
# Configure Poetry's settings for non-interactive installation and virtualenv creation
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version ${POETRY_VERSION} \
    && chmod a+x /opt/poetry/bin/poetry

# Set up the working directory
WORKDIR $PYSETUP_PATH

# Copy the project's dependency management files into the container
COPY ./poetry.lock ./pyproject.toml ./

# Install both development and runtime dependencies
RUN poetry install

# Set the working directory for the application code
WORKDIR /app
COPY . .

# Expose the port the app runs on
EXPOSE 8000


