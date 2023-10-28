#!/usr/bin/env python3

import sys
import subprocess

GATEWAY_MAPPING = {
    "att": "mms.att.net",
    "boost": "myboostmobile.com",
    "cricket": "mms.mycricket.com",
    "sprint": "pm.sprint.com",
    "tmobile": "tmomail.net",
    "tracfone": "mmst5.tracfone.com",
    "verizon": "vzwpix.com",
}

if len(sys.argv) < 4:
    print("Error: must specify phone number, provider, message, and repetitions, in that order. Available providers:")
    for provider in GATEWAY_MAPPING:
        print(provider)
    exit(1)

number = sys.argv[1]
gateway = GATEWAY_MAPPING[sys.argv[2]]
message = sys.argv[3]
repetitions = int(sys.argv[4])

for i in range(repetitions):
    subprocess.run(f"echo '{message}' | mailx {number}@{gateway}", shell=True, check=True)