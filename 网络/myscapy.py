from scapy.all import *
#导入scapy模块
def scan():
    print(show_interfaces(),"\n")
    ip=input("IP:")
    print("1:Intel(R) Wireless-AC 9462")
    print("2:Realtek PCIe GbE Family Controller")
    print("3:VMware Virtual Ethernet Adapter for VMnet2")
    print("4:自定义")
    x=int(input(""))
    if x==1:
        wifi="Intel(R) Wireless-AC 9462"
    elif x==2:
        wifi="Realtek PCIe GbE Family Controller"
    elif x==3:
        wifi="VMware Virtual Ethernet Adapter for VMnet2"
    elif x==4:
        wifi=input("自定义:")
    #选择抓包的网络接口
    tnet=ip+'/24'
    for i in range(0,1):
        #循环扫描
        p=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=tnet)
        #模拟包
        ans,unans=srp(p,iface=wifi,timeout=8,verbose=2)
        print(ans)
        print(unans)
        print("扫描到%d台主机："%len(ans))
        result=[]
        for s,r in ans:
            #解析收到的包，提取出需要的IP地址和MAC地址
            #r中包括ip与mac地址
            result.append([r.psrc,r.hwsrc])
        result.sort()
        #将获取的信息进行排序，看起来更整齐一点
        for ip,mac in result:
            print(ip,"\t----->\t",mac)
        end=input("回车退出,r重新扫描")
        if end == 'r':
            scan()
        else:
            pass

if __name__ == "__main__":
    scan()
    
 

# from scapy.all import *
# import time
# wifi="Realtek PCIe GbE Family Controller"
# #构造数据包 Ether()层可以省略构造内容,因为默认就是,当然可以写上,可以加快速度
# p=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.0.100/24")
# #数据包发送,srp同时收到响应数据包和不响应数据包,需要用两个变量来接收。
# #ans中有请求有响应,unans只有请求没有响应
# ans,unans=srp(p,iface=wifi,timeout=2)
# print("一共扫描到了%d个主机"%len(ans))
# result=[]
# #ans是元组的形式,可以测试ans[0],发现结果是元组的形式
# for s,r in ans:
#     result.append([r[ARP].psrc,r[ARP].hwsrc]) #把目标的IP以及MAC地址加入到新的列表
#     result.sort() #对列表进行排序
# #遍历列表,打印ip以及对应的mac地址
# for ip,mac in result:
#     print(ip,"--->",mac)

