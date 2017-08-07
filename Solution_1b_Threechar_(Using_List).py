import operator
from operator import itemgetter

def Check_String_Case(x):
      str1=''
      return x.lower()
      
def Check_Top_Three(X):
      count = 0
      L1 =[]
      for ch1 in X:
            for ch2 in X:
                  if ch1 in ch2:
                        count = count + 1
            if ch1 not in L1:
                  L1.append([ch1,count])
            count = 0
     
      L1.sort(key=operator.itemgetter(1))
      
      L3=[]
      for  x in range(len(L1)):
            if  L1[x][0] not in L3:    
                  L3.append(L1[x][0])
            
            
      L3=L3[-3:]
      L3.sort(key=operator.itemgetter(0))
      return L3        

X = input('Enter the String:')
X=Check_String_Case(X)
#print(X)
print(Check_Top_Three(X))




            
