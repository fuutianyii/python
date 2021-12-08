import subprocess        #加载支持Linux系统内部命令模块
import os
#定义函数，允许ping任何主机，ping函数需要给IP作为参数
def ping(host):
    rc = subprocess.call(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )            #定义ping命令的变量，返回值0:正常，返回值1：ping不通
    if rc:
        print('%s: down' % host)    #无法ping通打印down
    else:
        print('%s: up' % host)        #当re=0，表示可以ping通，打印up
if __name__ == '__main__':
    #生成整个网段的IP列表[172.40.58.1,172.40.58.2....]
    ips = ['172.40.58.%s' % i for i in range(1, 255)]
    for ip in ips:
        pid = os.fork()    # 父进程负责生成子进程
        if not pid:    # 子进程负责调用ping函数
            ping(ip)
            exit()        # 子进程ping完一个地址后结束，不要再循环