#coding:gbk
"""
import os
import sys
import socket
import ConfigParser

def reader(path):
    con = os.popen("cat %s"%path)
    content = con.read()
    con.close()
    return content

def connect(cont):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(("192.168.0.204",8000))
    sock.send(cont)
    sock.close()

def main():
    cfg = ConfigParser.ConfigParser()
    #cfg.read("")

if __name__ == "__main__":
    print(os.path.dirname(os.path.dirname(__file__)))
    print(os.path.join(os.path.dirname(__file__),"client_config.cfg")) 

"""
"""
import os
import sys
import socket
import ConfigParser

def reader(path):
    con = os.popen("cat %s"%path)
    content = con.read()
    con.close()
    return content
      1 #!/usr/bin/python
      2 #coding:utf-8
      3 
      4 import os
      5 import sys
      6 import socket
      7 import ConfigParser
      8 
      9 def reader(path):
     10     con = os.popen("cat %s"%path)
     11     content = con.read()
     12     con.close() 
     13     return content
     14         
     15 def connect(cont):
     16     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     17     sock.connect(("192.168.0.204",8000))
     18     sock.send(cont)
     19     sock.close()
     20     
     21 def main():
     22     cfg = ConfigParser.ConfigParser()
     23     #cfg.read("")
     24 
     25 if __name__ == "__main__":
     26     config_path = os.path.join(os.path.dirname(__file__),"client_config.cfg")
     27     cfg = ConfigParser.ConfigParser()
     28     cfg.read(config_path)
     29     path_dict = dict(cfg.items("PATH_CONFIG"))
     30     print(path_dict)
     31     read_path = path_dict["read_path"]
     32     path_list = path_dict["read_list"].split(",")
     33     print(read_path)
     34     print(path_list)



          25 if __name__ == "__main__":
     26     config_path = os.path.join(os.path.dirname(__file__),"client_config.cfg")
     27     cfg = ConfigParser.ConfigParser()
     28     cfg.read(config_path)
     29     path_dict = dict(cfg.items("PATH_CONFIG"))
     30     print(path_dict)
     31     read_path = path_dict["read_path"]
     32     path_list = path_dict["read_list"].split(",")
     33     for path in path_list:
     34         connect(reader(path))


"""

"""
def reader(path):
    con = os.popen("cat %s"%path)
    content = con.read()
    con.close()
    return content
      1 #!/usr/bin/python
      2 #coding:utf-8
      3 
      4 import os
      5 import sys
      6 import socket
      7 import ConfigParser
      8 
      9 def reader(path):
     10     con = os.popen("cat %s"%path)
     11     content = con.read()
     12     con.close() 
     13     return content
     14         
     15 def connect(cont):
     16     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     15 def connect(cont):
     15 def connect(cont):
      3 
      4 import os
      5 import sys
      6 import socket
      7 import ConfigParser
      8 
      9 def reader(path):
     10     con = os.popen("cat %s"%path)
     11     content = con.read()
     12     con.close()
     13     return content
     14 
     15 def connect(cont):
     16     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     17     sock.connect(("192.168.0.204",8000))
     18     sock.send(cont)
      7 import ConfigParser
      8 
      9 def reader(path):
     10     con = os.popen("cat %s"%path)
     11     content = con.read()
     12     con.close() 
     13     return content
     14 
     15 def connect(cont):
     16     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     17     sock.connect(("192.168.0.204",8000))
     18     sock.send(cont)
     19     sock.close()
     20 
     21 def main():
     22     cfg = ConfigParser.ConfigParser()
     22     cfg = ConfigParser.ConfigParser()
     23     
     24 def get_path(path):
     25     path_list = []
     26     if os.path.isdir(path):
     27         path_list += os.listdir(path)
     22     cfg = ConfigParser.ConfigParser()
     23 
     24 path_list  = []
     25 def get_path(path):
     26     global path_list
     27     if os.path.isdir(path):
     28         path_list += os.listdir(path)
     29     else:
     30         path_list.append(path)
     31     return path_list
     32 
     33 
     34 
     35 
     36 if __name__ == "__main__":
     37     config_path = os.path.join(os.path.dirname(__file__),"client_config.cfg")
     38     cfg = ConfigParser.ConfigParser()
     39     cfg.read(config_path)
     40     path_dict = dict(cfg.items("PATH_CONFIG"))
     41     path_lt = path_dict["read_list"].split(",")
     42     for path in path_lt: #两个路径
     43         print(get_path(path))


"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
#!/usr/bin/python
#coding:utf-8
"""
监控系统
"""

import os
import sys
import socket
import ConfigParser

def reader(path):
    con = os.popen("cat %s"%path)
    content = con.read()
    con.close()
    return content
      1 #!/usr/bin/python
      2 #coding:utf-8
      3 
      4 import os
      5 import sys
      6 import socket
      7 import ConfigParser
      8 
      9 def reader(path):
     10     con = os.popen("cat %s"%path)
     11     content = con.read()
     12     con.close() 
     13     return content
     14         
     15 def connect(cont):
     16     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     15 def connect(cont):
     15 def connect(cont):
      3 
      4 import os
      5 import sys
      6 import socket
      7 import ConfigParser
      8 
      9 def reader(path):
     10     con = os.popen("cat %s"%path)
     11     content = con.read()
     12     con.close()
     13     return content
     14 
     15 def connect(cont):
     16     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     17     sock.connect(("192.168.0.204",8000))
     18     sock.send(cont)
      7 import ConfigParser
      8 
      9 def reader(path):
     10     con = os.popen("cat %s"%path)
     11     content = con.read()
     12     con.close() 
     13     return content
     14 
     15 def connect(cont):
     16     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     17     sock.connect(("192.168.0.204",8000))
     18     sock.send(cont)
     19     sock.close()
     20 
     21 def main():
     22     cfg = ConfigParser.ConfigParser()
     22     cfg = ConfigParser.ConfigParser()
     23     
     24 def get_path(path):
     25     path_list = []
     26     if os.path.isdir(path):
     27         path_list += os.listdir(path)
     22     cfg = ConfigParser.ConfigParser()
     23 
     24 path_list  = []
     25 def get_path(path):
     26     global path_list
     27     if os.path.isdir(path):
     28         path_list += os.listdir(path)
     29     else:
     30         path_list.append(path)
     31     return path_list
     32 
     24 path_list  = []
     25 def get_path(path):
     26     global path_list
     27     if os.path.isdir(path):
     28         path_list += os.listdir(path)
     29     else:
     30         path_list.append(path)
     31     return path_list
     32 
     33 def get_path_dg(path):
     34     if os.path.isfile(path):
     35         return path
     36     else:
     37         for pa in os.listdir(path):
     38             get_path_dg(pa)
     39 
     30         path_list.append(path)
     31     return path_list
     32 
     33 def get_path_dg(path):
     34     if os.path.isfile(path):
     35         return path
     36     else:
     37         for pa in os.listdir(path):
     38             get_path_dg(pa)
     39 
     40 
     41 
     42 if __name__ == "__main__":
     43    get_path_dg("/proc")
     44     
     45  
     46  
     47  
     48  
     41 
     42 if __name__ == "__main__":
     31     return path_list
     32 
     33 
     34 
     35 
     36 
     37 dg_list = []
     38 def get_path_dg(path):
     39     if os.path.isfile(path):
     40         return path

"""




"""






"""

























