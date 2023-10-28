#!/usr/bin/env python3

import socket
import paramiko
import threading
import concurrent.futures


SERVERS = [
    "access1.computing.clemson.edu",
    "access2.computing.clemson.edu",
    "newton.computing.clemson.edu",
    "joey1.computing.clemson.edu",
    "joey2.computing.clemson.edu",
    "joey3.computing.clemson.edu",
    "joey4.computing.clemson.edu",
    "joey5.computing.clemson.edu",
    "joey6.computing.clemson.edu",
    "joey7.computing.clemson.edu",
    "joey8.computing.clemson.edu",
    "joey9.computing.clemson.edu",
    "joey10.computing.clemson.edu",
    "joey11.computing.clemson.edu",
    "joey12.computing.clemson.edu",
    "joey13.computing.clemson.edu",
    "joey14.computing.clemson.edu",
    "joey15.computing.clemson.edu",
    "joey16.computing.clemson.edu",
    "joey17.computing.clemson.edu",
    "joey18.computing.clemson.edu",
    "cerf1.computing.clemson.edu",
    "cerf2.computing.clemson.edu",
    "cerf3.computing.clemson.edu",
    "cerf4.computing.clemson.edu",
    "cerf5.computing.clemson.edu",
    "cerf6.computing.clemson.edu",
    "cerf7.computing.clemson.edu",
    "cerf8.computing.clemson.edu",
    "cerf9.computing.clemson.edu",
    "cerf10.computing.clemson.edu",
    "cerf11.computing.clemson.edu",
    "cerf12.computing.clemson.edu",
    "cerf13.computing.clemson.edu",
    "cerf14.computing.clemson.edu",
    "cerf15.computing.clemson.edu",
    "cerf16.computing.clemson.edu",
    "cerf17.computing.clemson.edu",
    "cerf18.computing.clemson.edu",
    "cerf19.computing.clemson.edu",
    "cerf20.computing.clemson.edu",
    "cerf21.computing.clemson.edu",
    "cerf22.computing.clemson.edu",
    "cerf23.computing.clemson.edu",
    "cerf24.computing.clemson.edu",
    "cerf25.computing.clemson.edu",
    "cerf26.computing.clemson.edu",
    "cerf27.computing.clemson.edu",
    "cerf28.computing.clemson.edu",
    "cerf29.computing.clemson.edu",
    "cerf30.computing.clemson.edu",
    "ada1.computing.clemson.edu",
    "ada2.computing.clemson.edu",
    "ada3.computing.clemson.edu",
    "ada4.computing.clemson.edu",
    "ada5.computing.clemson.edu",
    "ada6.computing.clemson.edu",
    "ada7.computing.clemson.edu",
    "ada8.computing.clemson.edu",
    "ada9.computing.clemson.edu",
    "ada10.computing.clemson.edu",
    "ada11.computing.clemson.edu",
    "ada12.computing.clemson.edu",
    "ada13.computing.clemson.edu",
    "ada14.computing.clemson.edu",
    "ada15.computing.clemson.edu",
    "babbage1.computing.clemson.edu",
    "babbage2.computing.clemson.edu",
    "babbage3.computing.clemson.edu",
    "babbage4.computing.clemson.edu",
    "babbage5.computing.clemson.edu",
    "babbage6.computing.clemson.edu",
    "babbage7.computing.clemson.edu",
    "babbage8.computing.clemson.edu",
    "babbage9.computing.clemson.edu",
    "babbage10.computing.clemson.edu",
    "babbage11.computing.clemson.edu",
    "babbage12.computing.clemson.edu",
    "babbage13.computing.clemson.edu",
    "babbage14.computing.clemson.edu",
    "babbage15.computing.clemson.edu",
    "babbage16.computing.clemson.edu",
    "babbage17.computing.clemson.edu",
    "babbage18.computing.clemson.edu",
    "babbage19.computing.clemson.edu",
    "babbage20.computing.clemson.edu",
    "babbage21.computing.clemson.edu",
    "babbage22.computing.clemson.edu",
    "babbage23.computing.clemson.edu",
    "babbage24.computing.clemson.edu",
    "babbage25.computing.clemson.edu",
    "babbage26.computing.clemson.edu",
    "babbage27.computing.clemson.edu",
    "babbage28.computing.clemson.edu",
    "babbage29.computing.clemson.edu",
    "babbage30.computing.clemson.edu",
    "babbage31.computing.clemson.edu",
    "babbage32.computing.clemson.edu",
    "babbage33.computing.clemson.edu",
    "babbage34.computing.clemson.edu",
    "babbage35.computing.clemson.edu",
    "babbage36.computing.clemson.edu",
    "cirrus1.computing.clemson.edu",
    "cirrus2.computing.clemson.edu",
    "cirrus3.computing.clemson.edu",
    "cirrus4.computing.clemson.edu",
    "cirrus5.computing.clemson.edu",
    "cirrus6.computing.clemson.edu",
    "cirrus7.computing.clemson.edu",
    "cirrus8.computing.clemson.edu",
    "cirrus9.computing.clemson.edu",
    "titan1.computing.clemson.edu",
    "titan2.computing.clemson.edu",
    "titan3.computing.clemson.edu",
    "titan4.computing.clemson.edu",
    "titan5.computing.clemson.edu",
]
PROXY = "access1.computing.clemson.edu"
USERNAME = "araza"
# KEY_FILE = "/home/ahmer/.ssh/id_ed25519"
KEY_FILE = "/home/ahmer/.ssh/id_ed25519"


def get_users(server_name: str, proxy: paramiko.SSHClient):
    # print(
    #     f"Proxy is {socket.gethostbyaddr(proxy.get_transport().sock.getpeername()[0])}"
    # )
    # If proxy parameter address and server name are the same, don't ssh
    if (
        socket.gethostbyaddr(proxy.get_transport().sock.getpeername()[0])[0]
        == server_name
    ):
        stdin, stdout, stderr = proxy.exec_command("who | awk '{print $1}' | sort -u")
    else:
        stdin, stdout, stderr = proxy.exec_command(
            f"ssh -o StrictHostKeyChecking=no -o ConnectTimeout=2 {server_name} who | awk '{{print $1}}' | sort -u"
        )

    stdout_str = stdout.read().decode()
    stderr_str = stderr.read().decode()
    return stdout_str, stderr_str


def check_servers():
    proxy = paramiko.SSHClient()
    proxy.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    proxy.connect(hostname=PROXY, username=USERNAME, key_filename=KEY_FILE)

    users: dict[str, str] = {}

    for server in SERVERS:
        result = get_users(server, proxy)
        print(f"{server:<40}", end="")
        if result[1] == "" or result[1].startswith("@" * 59):
            print(" ".join(result[0].split("\n")))
        else:
            print(f"ERROR: {result[1].strip()}")


if __name__ == "__main__":
    check_servers()
