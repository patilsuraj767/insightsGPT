FROM registry.redhat.io/ubi8/ubi-minimal

RUN microdnf install --disableplugin=subscription-manager --nodocs -y python3.11 python3.11-pip tar gzip gcc
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN pip3 install --upgrade pip
RUN pip3 install poetry

WORKDIR /app_root/src
COPY . .
RUN source ~/.profile && \
        poetry install
