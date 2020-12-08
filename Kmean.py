from sklearn.cluster import KMeans
from readPcap import readPcapFile
def getPoin(data):
    poin=[]
    for i in data:
        poin+=[[i[0],i[5]]]
    return poin
def PhanCumKmean(data):
    poin=getPoin(data)
    k=KMeans(n_clusters=3).fit(poin)
    i=0
    k0=[]
    k1=[]
    k2=[]
    for x in k.labels_:
        if x==0:
            k0+=[data[i]]
        if x==1:
            k1+=[data[i]]
        if x==2:
            k2+=[data[i]]
        i+=1
    return [k0,k1,k2]
# print(getPoin(getData(f)))
# f = open('bbb.pcap', 'rb')
# data=readPcapFile(f)
# x=PhanCumKmean(data)
# print(x[0][0])
