FROM ghcr.io/linuxserver/baseimage-ubuntu:jammy

# Adding trusting keys to apt for repositories

# Install dependencies
RUN apt-get -y update && \
    apt-get -y install wget python3 python3-pip

# Add google signature keys and chrome repo
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | tee /etc/apt/trusted.gpg.d/google.asc >/dev/null
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Install chrome
RUN apt-get -y update && \
    apt-get -y install google-chrome-stable


# Set display port as an environment variable
ENV DISPLAY=:99
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /root /
