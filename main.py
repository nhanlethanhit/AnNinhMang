from Kmean import PhanCumKmean
from readPcap import readPcapFile
import os
import datetime
s0=b'/poc2.flv'
s1=b'MZ\xe8\x00\x00\x00\x00[REU\x89\xe5\x81\xc3\xd6B\x00\x00\xff\xd3\x81\xc3#i\x02\x00\x89;Sj\x04P\xff\xd0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x0e\x1f\xba\x0e\x00\xb4\t\xcd!\xb8\x01L\xcd!This program cannot be run in DOS mode.\r\r\n$\x00\x00\x00\x00\x00\x00\x00\xbbE\xa8U\xff$\xc6\x06\xff$\xc6\x06\xff$\xc6\x06\xb9u'
s2=b'C\xb0\x02\x00'
packet_number=1
sig=[s0,s1,s2]
def CheckPacket(k):
    dem=0
    for packet in k:
        data_packet=packet[6]
        for s in sig:
            if s in data_packet:
                dem+=1
                if(dem>=packet_number):
                    dem=0
                    time=packet[0]
                    ip_src=packet[1]
                    ip_dst=packet[2]
                    print("PHÁT HIỆN TẤN CÔNG")
                    print("TIME:"+str(datetime.datetime.fromtimestamp(time))+", IP_SRC: "+ip_src+" ,IP_DST: "+ip_dst)
                break
while True:
    os.system("windump -i 4 -Avvvs0 -c 200 -w file1.pcap")
    f = open('file2.pcap', 'rb')
    data=readPcapFile(f)
    k=PhanCumKmean(data)
    CheckPacket(k[0])
    CheckPacket(k[1])
    CheckPacket(k[2])
    f.close()
    