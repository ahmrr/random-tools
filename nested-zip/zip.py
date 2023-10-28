import os
import sys
import shutil
import zipfile
import subprocess

if len(sys.argv) < 4:
    print("Error: levels, output file, and input file(s) not specified")
    exit(1)

levels = int(sys.argv[1])
print(f"Levels: {levels}")
out_file = sys.argv[2]
print(f"Output file: {out_file}")
in_files = sys.argv[3:]
print(f"Input files: {in_files}")

try:
    if not os.path.exists("dump"):
        os.mkdir("dump")
except:
    print('Error: could not create directory "dump"')
    exit(1)

print(f"Zipping level 1...")
with zipfile.ZipFile(f"{out_file}", "w", zipfile.ZIP_DEFLATED) as zf:
    for file in in_files:
        zf.write(file)

for level in range(1, levels):
    print(f"Zipping level {level + 1}...")
    with zipfile.ZipFile(f"dump/{out_file}", "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(f"{out_file}", arcname=out_file)
    shutil.move(f"dump/{out_file}", out_file)

try:
    shutil.rmtree("dump")
except:
    print('Error: could not remove directory "dump"')
    exit(1)

print("Zipped!")
