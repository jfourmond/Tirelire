#
# Use python 3.10.9 image
# https://hub.docker.com/_/python/
#
FROM python:3.10.9-slim

#================================================

LABEL version="0.1"
LABEL build="2022-12-17"
LABEL description="La Tirelire"
LABEL maintainer="Jérôme FOURMOND <jerome@fourmond.fr>"

#================================================

WORKDIR /usr/src/app/

RUN cat /etc/os-release

#=============================================================================#
#             Installation des paquets linux nécessaires                      #
#=============================================================================#

RUN apt-get update
RUN apt-get install -y curl libpq-dev python3-dev
RUN apt-get -y install gcc mono-mcs && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

#=============================================================================#
#                        Installation de Dockerize                            #
#=============================================================================#

RUN curl -sfL $(curl -s https://api.github.com/repos/powerman/dockerize/releases/latest | grep -i /dockerize-$(uname -s)-$(uname -m)\" | cut -d\" -f4) | install /dev/stdin /usr/local/bin/dockerize

#================================================
#     Installation des dépendances python       #
#================================================

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#================================================

ADD bank bank
ADD piggy_bank piggy_bank
COPY manage.py ./

#================================================

ENTRYPOINT [ "python" ]
CMD [ "manage.py", "runserver"]
