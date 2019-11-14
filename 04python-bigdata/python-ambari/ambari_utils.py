#coding=utf-8
'''
参考： https://github.com/apache/ambari/blob/trunk/ambari-server/docs/api/v1/
'''

import requests,json
import time
ambari_ip=""

cluster_name="";
user=""
passwd=""

#"http://your.ambari.server/api/v1/clusters/c1 ,拼接处基本的请求url
control_url="http://{}:8080/api/v1/clusters/{}/hosts".format(ambari_ip,cluster_name)
AUTH=(user,passwd)

'''
请求体参数获取方法：
 f12 打开调试模式：
   network页签
 点击请求：
   同时查看network 页签内的请求。
   右键 选择 copy as curl （bash）
   
 将这些参数封装起来（有部分不是非必要参数，不必填写）

'''
def startComponents(host,component):
    start_component_url= control_url + "/{}/host_components/{}".format(host,component)
    headers={ 'X-Requested-By': 'X-Requested-By'}
    body ={ "RequestInfo": {
                             "context": "{} {}".format( "start",component),
                             "operation_level": {
                                                  "level": "HOST_COMPONENT", "cluster_name": "{}".format(cluster_name),
                                                  "host_name": "{}" .format(host),"service_name" : "{}".format(component)
                                                 }
                            },
            "Body" :{
                     "HostRoles":{
                                    "state":"INSTALLED"
                                 }

                     }
          }
    data=json.dumps(body)
    r=requests.put(start_component_url,data=data,auth=AUTH,headers=headers)
    print(r.json())

'''

获取某个节点，某个服务的状态
GET /clusters/c1/hosts/host1/host_components/DATANODE
'''

def getComponentStatus(host,component):

    get_component_status_url =control_url+"/{}/host_components/{}".format(host,component)

    try:
        rep=requests.get(get_component_status_url,auth=AUTH)
        if(rep.status_code==200):
            jsonrep=json.loads(rep.text)
            status=jsonrep['HostRoles']['state']
            return status
        else:
            print("==============logging")
    except Exception as e:
            print("==============logging")


def getHostComponentsStatus(host):
    '''

    :param host:
    :return: component_dict  组件与其状态
             status          当前节点状态是否符合期望，
             getStatus     是否获取到了状态

    '''
    component_dict= {}
    status = True
    getStatus=True

    get_host_components_status_url=control_url +"/{}/host_components".format(host)

    try:
        rep = requests.get(get_host_components_status_url,auth=AUTH)
        #如果状态码是20x 则获取成功
        print (rep.status_code)
        if(str(rep.status_code).startswith("20")):
            jsonrep=json.loads(rep.text)
            items=jsonrep['items']
            for itemjson in items:
                item=itemjson['HostRoles']['component_name']

                #排除client 角色，与SQOOP等一直是启动状态的客户端，这些不需要启动，也不需要判断状态
                if "CLIENT" not in item and "SQOOP" not in item:
                    compent_status=getComponentStatus(host,item)
                    component_dict[item]=compent_status

                    #这里不能认为状态为INSTALLED (关闭）则没有启动成功，只要是非STARTED 都是没有成功
                    if(compent_status !="STARTED"):
                        status=False
                        if compent_status=="UNKNOWN":
                        #如果这里是UNKNOWN 则代表没有获取到状态
                            getStatus=False
        else:
            #没有正常获取到状态
            print("=======logging")
            getStatus=False
            status=False

    except Exception as e:
        status=False
        getStatus=False

    return component_dict,status,getStatus



# INSTALLED : 关闭  STARTED: 开启
def changeHostComponents(host,target_status):
    '''

    :param host:   传入的hostname
    :param target_status:   需要改为的状态
    :return:
    '''

    #获取组件状态
    component_dict,status,getStatus=getHostComponentsStatus(host)
    print("获取组件状态 {} {} ".format(getStatus,component_dict))
    count=0
    #这里的count 是用来获取不到状态的时候重试的。

    while count < 5 & (getStatus==False):
        time.sleep(60)
        component_dict,status,getStatus=getHostComponentsStatus(host)
        print("第{} 次 获取组件状态{}".format(count+1,component_dict))
        count=count+1
    #再等待最后的时间
    if getStatus==False:
        time.sleep(300)
        component_dict,status,getStatus=getHostComponentsStatus(host)
        print("等待{} 后获取组件状态{} {}  ".format("300",getStatus,component_dict))

    if getStatus==False:
        raise Exception("=========error info ====")

    '''
        如果是 INSTALLED --- 将非INSTALLED的关闭, STARTED---将非 STARTED的开启
        '''
    # 将与status 相同的封装到操作列表中
    opera_com_dict = []
    for compk, comps in component_dict.items():
        if comps == target_status:
            pass
        else:
            opera_com_dict.append(compk)

    # 判断需要操作的组件是否为空
    if (len(opera_com_dict) < 1):
        print("所有组件的状态已经与目标状态一致...")
        return
    else:
        # 要操作的组件list 拼接为字符串，封装到请求中
        comp_string = ','.join(str(n) for n in opera_com_dict)
        print (comp_string)
        change_compent_url = control_url + "/{}/host_components".format(host)

        print(change_compent_url)
        headers = {

            'X-Requested-By': 'X-Requested-By'
        }

        body = {"RequestInfo": {"context": " {} {} 所有组件".format(target_status, host),
                                "operation_level": {"level": "HOST", "cluster_name": "{}".format(cluster_name),
                                                    "host_names": "{}".format(host)},
                                "query": "HostRoles/component_name.in({})".format(comp_string)},
                "Body": {"HostRoles": {"state": "{}".format(target_status)}}
                }

        try:
            data = json.dumps(body)
            rep = requests.put(change_compent_url, data=data, auth=AUTH, headers=headers)
            print (rep.status_code)
            print (rep.text)
            print(rep.json())

        except Exception as e:
            print("error {} ".format(e))
