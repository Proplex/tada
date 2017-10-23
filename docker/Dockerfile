FROM ubuntu:16.04
MAINTAINER Keith Carolus (kmcarolu@buffalo.edu)

#  _______    _____        
# |__   __|  |  __ \       
#    | | __ _| |  | | __ _ 
#    | |/ _` | |  | |/ _` |
#    | | (_| | |__| | (_| |
#    |_|\__,_|_____/ \__,_|
#                          

# to build
# > docker build -t tada_flask_image /path/to/dir/with/this/file

# to run
# > docker run -d --name=tada_flask_server --network=host -P tada_flask_image

# open browser and go to http://0.0.0.0/
# you should see TaDa :)

# to attach
# > docker exec -it tada_flask_server /bin/bash

# to shut down
# > docker stop tada_flask_server
# to restart after restarting computer
# > docker start tada_flask_server

# tada_user's password is tada_user

ENV DEBIAN_FRONTEND=noninteractive

RUN apt -y update && apt -y upgrade && apt install -y -q --no-install-recommends \
    vim \
    git \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-pymysql \
    mysql-server \
    mysql-client && \
    pip3 install --upgrade pip && \
    pip3 install Flask && \
    pip3 install Flask-Assets

# flask environmental variables
ENV LC_ALL C.UTF-8
ENV LANG=C.UTF-8

RUN chown -R mysql:mysql /var/lib/mysql
RUN git clone https://github.com/CosmicVarion/tada /tada
RUN cd /tada && git checkout develop

