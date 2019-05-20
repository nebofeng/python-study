#coding:utf-8
def get_info(path):
    info={}
    config=open(path)
    for line in config:
        result=[ele.strip() for ele in line.split('=')]
        info.update(dict([result]))
    return info



if __name__=='__main__':
    info=get_info(r'./data.log')
    print(info)
