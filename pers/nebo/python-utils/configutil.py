import configparser
import os

class ConfigUtil:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None,filename=None):
        if filepath:
            configpath = filepath
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            print(root_dir)
            configpath = os.path.join(root_dir, "config")
            if filename:
                configfile = os.path.join(configpath, filename)
                print(configpath)
            else:
                print(configpath)
                configfile = os.path.join(configpath, "config.conf")
        self.cf = configparser.ConfigParser()
        self.cf.read(configfile)



    #获取参数
    def get_param(self, option,param):
        value = self.cf.get(option, param)
        return value


if __name__=='__main__':
        configUtil =   ConfigUtil()
