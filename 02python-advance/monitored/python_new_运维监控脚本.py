#coding:gbk

#1����ȡҪ��صļ��������Ϣ
    #os.system("command")
    #os.popen("command")
    #file open("/proc/file")
        #�ַ���Ҫ����
            #ע��������� \n
            #��������
                # +
                # join
                # "%s"%str
                # ("{}").format(a)
        #·���Ĵ���
            #os.path
        #�ļ�����Ĵ���
            #read
            #readline
            #readlines
        #Python�������������͵�ת��
            #int
            #str
            #list
            #dict
            #tuple
        #��ص�Ŀ��
            #cpu
            #�ڴ�
            #����
            #ϵͳ�Ľ���
        #��صķ�ʽ
            #1����������֮ǰ��os,sys,file
            #2��psutil
                #1����һ����ƽ̨�Ŀ�
                #2�����Ի�ȡ��ϵͳ���еĽ��̺�ϵͳ������
                #3���������Ϊ�˼�س��ֵ�

                #cpu
                    #User Time ִ���û����̵�ʱ��ٷֱ�
                    #System Time ִ���ں˽��̺��жϵ�ʱ��ٷֱ�
                    #Wait IO ����ʱ���
                    #idle cpu����idle״̬��ʱ��ٷֱ�
                        #cpu_times ����cpu��������Ϣ
                            #percpu Ĭ��Ϊfalse
                            #percpu ΪTrue ���ض�����б���ʽ
                            #cpu_times(percpu = True)����
                        #cpu_count ����cpu�߼�����
                            #logical����Ĭ��ΪTrue
                            #��logical����ΪFalse���ص����������
                #�ڴ�
                    #�ڴ������(total)
                    #�Ѿ�ʹ�õ��ڴ���(used)
                    #���е��ڴ���(free)
                    #����ʹ����(buffers)
                    #����ʹ������cache��
                    #��������ʹ����(swap)
                        #virtual_memory() �����ڴ��������Ϣ
                #����
                    #���̵�������     
                    #IO��Ϣ
                        #disk_partitions() ��ȡ���̵�������Ϣ
                        #disk_usage() ��÷�����ʹ�����
                        #disk_io_counters() ��ȡ�����ܵ�io����
                            #perdisk Ĭ��ΪFalse
                            #ΪTrue ���ص���������io����
                #ϵͳ�Ľ���
                    #pids ����ϵͳ����pid
                    #Process ����һ��process���󣬲���Ϊ���̵�pid
                        #p = psutil.Process(1)
                    #p.name() ������̵�����
                    #p.exe() ���ؽ���bin�ļ�λ��
                    #p.cwd() ���̵Ĺ���Ŀ¼�ľ���·��
                    #p.status() ���ؽ��̵�״̬
                    #p.create_time() ���̵Ĵ���ʱ�䣬ʱ���
                        #time.ctime()��ʱ���ת��Ϊ�ַ���ʱ��
                    #p.uids() ���ؽ��̵�uid��Ϣ
                    #p.gids() ���ؽ��̵�gid��Ϣ
                    #p.cpu_times() ����cupʱ����Ϣ
                    #p.memory_info() ���ؽ����ڴ��������
                    #p.io_counters() ���ؽ��̵�io��д��Ϣ
                    
import urllib
import urllib2
test_data = {'ServiceCode':'aaaa','b':'bbbbb'}#�����ֵ乹���������ݵĸ�ʽ
test_data_urlencode = urllib.urlencode(test_data)#�������õ����ݽ��б��� json
requrl = "http://192.168.81.16/cgi-bin/python_test/test.py"
req = urllib2.Request(url = requrl,data =test_data_urlencode)#Я�����ݷ�������














        











                







