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
# docker run -d \
#            --name=tada_flask_server \
#            --network=host \
#            --env="DISPLAY" \
#            --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
#            -P \
#            tada_flask_image \
#            /bin/bash -c "while true; do echo running; sleep 10; done"
# or
# docker run -d --name=tada_flask_server --network=host --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix" -P tada_flask_image /bin/bash -c "while true; do echo running; sleep 10; done"

# to attach
# > docker exec -it tada_flask_server /bin/bash
# then
# > FLASK_APP=/home/tada_user/tada/flask/app.py flask run
# tada_user's password is tada_user
# open browser and go to http://localhost
# you should see TaDa :)

# to shut down
# > docker stop tada_flask_server
# to restart after restarting computer
# > docker start tada_flask_server

ENV DEBIAN_FRONTEND=noninteractive

RUN apt -y update && apt -y upgrade && apt install -y -q --no-install-recommends \
    vim \
    sudo \    
    git \
    curl \
    gedit \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-pymysql \
    mysql-server \
    mysql-client && \
    pip3 install --upgrade pip && \
    pip3 install Flask

# flask environmental variables
ENV LC_ALL C.UTF-8
ENV LANG=C.UTF-8

# set root password to tada_user
# create tada_user
# set mluser password to tada_user
# add tada_user to sudoers and www-data
RUN echo "root:tada_user" | chpasswd && \
    useradd -ms /bin/bash tada_user && \
    echo "tada_user:tada_user" | chpasswd && \
    adduser tada_user sudo && \
    adduser tada_user www-data 

RUN git clone https://github.com/CosmicVarion/tada /home/tada_user/tada

RUN chown -R tada_user /home/tada_user
WORKDIR /home/tada_user
USER tada_user

