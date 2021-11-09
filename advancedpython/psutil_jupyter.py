#!/usr/bin/env python
# coding: utf-8

import socket
import psutil
import sys

def python_version():
    return sys.version_info

def ip_addresses():
    hostname = socket.gethostname()

    adresses = socket.getaddrinfo(hostname, None)
    address_info = []
    for adress in adresses:
        address_info.append(adress[0].name, adress[4][0])
    return address_info

def cpu_stats():
    return psutil.cpu_stats()

def cpu_load():
    return psutil.cpu_percent(interval=0.1)

def cpu_count():
    return psutil.cpu_count()

def cpu_virtual_memory():
    return psutil.virtual_memory()

def cpu_users():
    return psutil.users()

def pids():
    return psutil.pids()

def swap_memory():
    return psutil.swap_memory()

def load_avg():
    return psutil.getloadavg()

def boot_time():
    psutil.boot_time()

def connections():
    return psutil.net_connections()





