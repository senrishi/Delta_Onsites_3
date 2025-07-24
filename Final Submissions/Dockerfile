FROM ubuntu:latest
WORKDIR /app
COPY setenv.sh .
RUN chmod +x setenv.sh
COPY templates .
COPY response.py .

RUN apt-get update && \
    apt-get install -y apache2 python3 python3-pip
RUN pip3 install Flask

COPY app.conf /etc/apache2/sites-available/app.conf
COPY login.html /etc/apache2/sites-available/login.html
EXPOSE 80

RUN a2enmod proxy proxy_http proxy_balancer lbmethod_byrequests && \
    a2ensite app.conf
CMD ["/setenv.sh"]
    