#!/usr/bin/env python3
import os
import time
import datetime

MY_DOMAIN = "https://my-domain.com"
DIR = "/opt/wp_docker_ubuntu"

date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
stream = os.popen(f'curl -sSf {MY_DOMAIN} > /dev/null && echo "success"')
output = stream.read()
time.sleep(1.5)

if "success" in output:
    os.popen(f'echo "OK -> {date_time}" >> {DIR}/health_check_log.txt')
else:
    os.popen('cd {DIR} && docker-compose -f docker-compose-ssl-ready.yaml down')
    os.popen('cd {DIR} && docker-compose -f docker-compose-ssl-ready.yaml up')
    os.popen(f'echo "NOT OK! Restared -> {date_time}" >> {DIR}/health_check_log.txt')