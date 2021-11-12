#!/usr/bin/env python
# coding: utf-8

import socket
import psutil
import sys

HELP_TEXT = """порядок вызова: python {program_name:s}

Отображение значения датчиков

Флаги и аргументы:

--help: вывести это сообщение"""

def python_version():
    return sys.version_info

def ip_addresses():
    hostname = socket.gethostname()

    adresses = socket.getaddrinfo(socket.gethostname(), None)
    address_info = []
    for adress in adresses:
        address_info.append((adress[0].name, adress[4][0]))
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

def ram_available():
    return psutil.virtual_memory().available

def connections():
    return psutil.net_connections()

def show_sensors():
    print("Версия Python: {0.major}.{0.minor}".format(python_version()))
    for address in ip_addresses():
        print("IP-адреса: {0[1]} ({0[0]})".format(address))
    print("Загрузка ЦП: {:.1f}".format(cpu_load()))
    print("Доступная память: {} MiB".format(ram_available() / 1024**2))

def command_line(argv):
    program_name, *arguments = argv
    if not arguments:
        show_sensors()
    elif arguments and arguments[0] == '--help':
        print(HELP_TEXT.format(program_name=program_name))
        return
    else:
        raise ValueError("Неизвестные аргументы {}".format(arguments))

if __name__ == '__main__':
    command_line(sys.argv)