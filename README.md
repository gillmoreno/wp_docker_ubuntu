# A boilerplate code for using Wordpress with Docker

## Prerequisites
- A machine with docker installed on it
- A domain name that substitues **example.com**

## Some notes
- You need to create the .env file (and place it at the same level as docker-compose.yaml) with at least the following variables:
    - MYSQL_ROOT_PASSWORD=WHATEVER
    - MYSQL_USER=WHATEVER
    - MYSQL_PASSWORD=WHATEVER
    - DOMAIN=WHATEVER
    - CERTBOT_EMAIL=WHATEVER
- In order to make the Health Check work:
    - the whole WP folder needs to belong the non root user that normally uses Docker
    - the python script needs to be executable (chmod -x)
    - a crontab needs to run every X minutes (depending on the max downtime the service can allow)

