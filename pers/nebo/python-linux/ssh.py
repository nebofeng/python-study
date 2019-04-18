import paramiko

client =  paramiko.SSHClient()#实例化一个SSH远程登录对象
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#防止没有密匙的情况
client.connect(
    "192.168.192.10",#host  ssh remote ip
    22,# port
    username="root",# username
    password="admin123.", #password
    timeout=1 # timeout connection time
   )
ins,out,err=client.exec_command("cd /home ;ls") # run commond return three param : (stdin,stddout,stderr)
for i in out.readlines():
    print(i)

client.close()# close connection
