import paramiko


def getSsh(ip,usename,password):
    # 把要连接的机器添加到known_hosts文件中
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=ip, port=22, username=usename, password=password)
    return ssh
    # cmd = 'ps'
    # # cmd = 'ls -l;ifconfig'       #多个命令用;隔开
    # stdin, stdout, stderr = ssh.exec_command(cmd)
    # result = stdout.read()
    #
    # if not result:
    #     result = stderr.read()
    # ssh.close()

def closeSsh():
    ssh.close