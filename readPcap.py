import dpkt
from dpkt.ip import IP
from dpkt.ethernet import Ethernet
import socket
def readPcapFile(file):
    data=[]
    # i=0
    pcap = dpkt.pcap.Reader(file)
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        try:
            if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
                continue
            ip_src=socket.inet_ntoa(ip.src)
            ip_dst = socket.inet_ntoa(ip.dst)
            sport=ip.data.sport
            dport=ip.data.dport
            packet_len=buf.__len__()
            # a="STT: "+str(i)+" ,IP SRC:"+str(ip_src)+" ,IP DST:"+str(ip_dst)+" ,SPORT:"+str(sport)+" ,DPORT:"+str(dport)+" ,LEN:"+str(packet_len)
            poin=[[ts,ip_src,ip_dst,sport,dport,packet_len,buf]]
            # print(a)
            # if s in buf:
            #     print(a)
            #     print(buf)
            # i+=1
            data+=poin
        except :
            pass 
    return data
# f = open('file2.pcap', 'rb')
# data=readPcapFile(f)
        
            