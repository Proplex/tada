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
# > docker run -d -p 80:80 --name tada_server --hostname tada_server tada_image /bin/bash -c "while true; do echo running; sleep 10; done"
# to attach
# > docker exec -it tada_server /bin/bash
# then
# > sudo service apache2 restart
# tada_user's password is tada_user
# open browser and go to http://0.0.0.0
# you should see TaDa :)

# to shut down
# > docker stop tada_server
# to restart after restarting computer
# > docker start tada_server

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
    mysql-client \
    curl

# manually set apache environmental variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# expose port 80
EXPOSE 80

# enable CGI
RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/cgi.load

ADD virt_tada.conf /etc/apache2/sites-enabled/000-default.conf

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

RUN chgrp -R www-data /home/tada_user/tada/* && \
    chmod +rx /home/ && \
    chmod +rx /home/tada_user/ && \
    chmod +rx /home/tada_user/tada/ && \
    chmod 755 /home/tada_user/tada/cgi_bin/

RUN chown -R tada_user /home/tada_user
WORKDIR /home/tada_user
USER tada_user

# CMD /usr/sbin/apache2ctl -D FOREGROUND

