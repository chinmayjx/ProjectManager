import os
import sys

in_dir = os.path.join('data', sys.argv[1])
out_dir = os.path.join('output', sys.argv[1])
if not os.path.exists(out_dir):
    os.mkdir(out_dir)
curr_vdo = ""
descr = ""
files = ""


def extract_clip(cmd):
    global files
    os.system(
        f'ffmpeg -y -ss {cmd[1]} -to {cmd[2]} -i {curr_vdo} -c copy {os.path.join(out_dir, cmd[0] + ".mp4")}')
    files += "file '" + cmd[0] + ".mp4'\n"


def parse_cmd(cmd):
    global curr_vdo, descr
    if cmd[0] == '_file':
        curr_vdo = os.path.join(in_dir, cmd[1])
    else:
        descr += cmd[0].replace("_", " ") + " " + cmd[1] + " " + cmd[2] + "\n"
        extract_clip(cmd)


with open(os.path.join(in_dir, 'table.txt'), 'r') as f:
    for line in f.readlines():
        row = line.strip().split(" ")
        parse_cmd(row)

with open(os.path.join(out_dir, "description.txt"), "w") as f:
    f.write(descr)
with open(os.path.join(out_dir, "files.txt"), "w") as f:
    f.write(files)
