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
# > docker build -t tada_image /path/to/dir/with/this/file
# to run
# > docker run -d --name tada_server --hostname tada_server tada_image /bin/bash -c "while true; do echo running; sleep 10; done"
# to attach
# > docker exec -it tada_server /bin/bash

# to shut down
# > docker stop tada_server
# to restart after restarting computer
# > docker start tada_server

# tada_user's password is tada_user

ENV DEBIAN_FRONTEND=noninteractive

RUN apt -y update && apt -y upgrade && apt install -y -q --no-install-recommends \
    vim \
    sudo \    
    git \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-pymysql \
    apache2 \
    mysql-server \
    mysql-client 

# set root password to tada_user
# create tada_user
# set mluser password to tada_user
# add tada_user to sudoers
RUN echo "root:tada_user" | chpasswd && \
    useradd -ms /bin/bash tada_user && \
    echo "tada_user:tada_user" | chpasswd && \
    adduser tada_user sudo 

RUN chown -R tada_user /home/tada_user
WORKDIR /home/tada_user
USER tada_user

RUN git clone https://github.com/CosmicVarion/tada
