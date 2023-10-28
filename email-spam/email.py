#!/usr/bin/env python3

import os
import sys
import random
import subprocess

NL = "\n"

if len(sys.argv) < 3:
    print(
        "Error: must specify sender name, sender username, receiver address, and repetitions, in that order."
    )
    exit(1)

sender_name = sys.argv[1]
sender_user = sys.argv[2]
receiver = sys.argv[3]
repetitions = int(sys.argv[4])

for i in range(repetitions):
    subprocess.run(
        f"echo '{('L' * 7 + NL) * 1024}' | mailx -a 'From: {sender_name} <{sender_user}@clemson.edu>' -a 'Reply-To: araza@g.clemson.edu' -s '{random.randint(0, 1000000000)}' {receiver}",
        shell=True,
        check=True,
    )
