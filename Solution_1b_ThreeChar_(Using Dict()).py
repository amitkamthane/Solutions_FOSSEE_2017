import operator
def Top_3(string):
    dic={}
    for x in string:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1
    #print dic
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
    #print sorted_dic
    size=len(sorted_dic)
    alpha=[]
    alpha.append(sorted_dic[size-1][0])
    alpha.append(sorted_dic[size-2][0])
    alpha.append(sorted_dic[size-3][0])
    alpha.sort()
    print(alpha)

x=input('Please Enter the String:')
Top_3(x)
