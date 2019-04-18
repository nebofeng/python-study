import subprocess, signal,os
p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
out, err = p.communicate()
# gives you ps -A's output in the out variable (a string). You can break it down into lines and loop on them...:

for line in out.splitlines():
    if 'iChat' in line:
        pid = int(line.split(None, 1)[0])
        os.kill(pid, signal.SIGKILL)