import optparse 
o=optparse.OptionParser()
o.add_option('-a',type='int',dest='a')
aa,b=o.parse_args()
print(aa.a)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-g','--gateway',dest="gateway")
args = parser.parse_args()
gateway_ip = args.gateway
print(gateway_ip)