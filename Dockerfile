FROM dynamath/dyna_env:latest

RUN pip install pyvirtualdisplay

RUN apt-get update && apt-get install -y \
    libglu1-mesa-dev \
    xvfb\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

VOLUME [ "/app" ]

COPY . .



