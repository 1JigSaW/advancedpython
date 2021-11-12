#!/usr/bin/env python
# coding: utf-8

import click
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

@click.command(help='Отображает значения датчиков')
def show_sensors():
    click.secho("Версия Python: ", bold=True, nl=False)
    click.echo("{0.major}.{0.minor}".format(python_version()))
    for address in ip_addresses():
        click.secho("IP-адреса: ", bold=True, nl=False)
        click.echo("{0[1]} ({0[0]})".format(address))
    click.secho("Загрузка ЦП: ", bold=True, nl=False)
    click.echo("{:.1f}".format(cpu_load()))
    click.secho("Доступная память: ", bold=True, nl=False)
    click.echo("{} MiB".format(ram_available() / 1024**2))

if __name__ == '__main__':
    show_sensors()