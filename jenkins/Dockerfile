FROM jenkins/jenkins:latest

USER root

RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-venv \
    && apt-get install -y wget unzip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

ENV ALLURE_VERSION 2.17.0

RUN wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.zip -O /tmp/allure.zip && \
    unzip /tmp/allure.zip -d /opt && \
    rm /tmp/allure.zip && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure

USER jenkins
