import operator
def sec_high(L1):
      
      L1.sort(key=operator.itemgetter(1))    #Sort List with respective Marks
      
      
      L2 = []                   #Loop Removes  all first Lowest Element 
      for x in range(len(L1)):
            if L1[x][1] == L1[0][1]:
                  print(end='')
            else:
                  L2.append([L1[x][0],L1[x][1]])
      #print(L2)

      L3 = []  
      count = 0   #Loop Searches for all the second lowest elements
      for x in range(len(L2)):
            if L2[x][1] == L2[0][1]:
                  L3.append(L2[x][0])
                  count = count +1
                  
            else: 
                  print('',end='')
      print(L3)   #Print List of Second Lowest elements
L=[['Harish', 37.21], ['Shakti', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]            
sec_high(L)

