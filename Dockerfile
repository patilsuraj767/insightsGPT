FROM fedora

RUN dnf group install "Development Tools" -y
RUN dnf install python3.11 python3.11-devel python3.11-pip tar gzip gcc gcc-c++ iputils -y
RUN dnf update -y
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN pip3 install --upgrade pip
RUN pip3 install poetry

WORKDIR /app_root/src
COPY pyproject.toml poetry.lock ./

RUN source ~/.profile && \
        poetry install

COPY . .
