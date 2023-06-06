ip=[int(x) for x in input().split()]
map={}
list=[]
for i in range(len(ip)):
    if ip[i] in map:
        map[ip[i]]+=1;
    else:
        map[ip[i]]=1
        list.append(ip[i])
for x in list:
    if map[x]>1:
        print(x)
        break