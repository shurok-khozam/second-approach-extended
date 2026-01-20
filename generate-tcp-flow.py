# This file is used for testing purposes only_

import time
import os
import subprocess
import requests

# Network
network_dir = os.getcwd() + "/network"
network_entrypoint = f'{network_dir}/EntryPoint.py'
network_command = f'python3 {network_entrypoint} --attackers [ATTACKERS] --unified-host-bandwidth=[HOST_BW] --unified-switch-bandwidth=[SWITCH_BW] --manuel-receivers'

# API
api_link = "http://localhost:5000"

# Hosts
server_host = 'hs'
normal_hosts = []
for i in range(1, 7):
    normal_hosts.append(f'h{i}')

# VARS
transmission_time = 40
transmission_time_ms = 40 * 1000

def sleep_seconds(time_s):
    seconds = 0
    while seconds < time_s:
        print('.', end='', flush=True)
        time.sleep(1)
        seconds = seconds + 1
    print('')

if __name__ == '__main__':
    run_network_cmd = network_command
    run_network_cmd = run_network_cmd.replace('[ATTACKERS]', f'[]').replace('[HOST_BW]', f'3.1').replace('[SWITCH_BW]', f'3.1')
    network_subprocess = subprocess.Popen(run_network_cmd, shell=True, stdin=subprocess.PIPE)
    sleep_seconds(10)
    print("(Generator) --> Network started")
    #####################################################
    # Starting tcp receiver
    requests.get(f'{api_link}/reset-tcp-receivers')
    print("(Generator) <---> Server Started")
    sleep_seconds(2)

    # Sending from all normal hosts to server
    destination_host = server_host
    for source_host in normal_hosts:
        requests.get(f'{api_link}/start-tcp-flow/{source_host}/{destination_host}/{transmission_time_ms}')
        print(f"(Generator) <---> Starting tcp sender from {source_host} to {destination_host}")


    sleep_seconds(transmission_time)

    requests.get(f'{api_link}/stop-all-tcp-flows')
    print("(Generator) <---> Stopping all tcp senders")

    interfaces_to_get = {
        "s0": ['s0-eth0'],
        "s1": ['s1-eth0'],
        "s2": ['s2-eth0'],
        "s3": ['s3-eth0'],
        "s4": ['s4-eth0'],
        "s5": ['s5-eth0'],
        "s6": ['s6-eth0'],
        "s101": ['s101-eth1', 's101-eth0', 's102-eth2'],
        "s102": ['s102-eth3', 's102-eth0'],
        "s103": ['s103-eth4', 's103-eth0', 's104-eth5'],
        "s104": ['s104-eth6', 's104-eth0']
    }

    for switch in interfaces_to_get.keys():
        for interface in interfaces_to_get[switch]:
            stats = requests.get(f'{api_link}/get-switch-statistics/{switch}/{interface}')
            print(f"(Generator) <-----> Switch {switch} : interface {interface}:")
            print(stats.text)

    for host in normal_hosts:
        stats = requests.get(f'{api_link}/get-host-ifconfig/{host}')
        print(f"(Generator) <-----> Host {host}")
        print(stats.text)

    print("(Generator) <--> Wait for TShark")
    sleep_seconds(10)

    #####################################################
    network_subprocess.communicate(input="exit\n".encode('ascii'), timeout=4)
    sleep_seconds(4)
    print("(Generator) <-- Network stopped")

