i = [['Harish', 37.21], ['Shakti', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
def SecondHighest(x):
    #Implementing a sort
    for i in range(0,len(x)):
        for j in range(0,len(x)-1):
            #print x[j],x[j+1]
            if(x[j][1]>x[j+1][1]):
                temp=x[j]
                x[j]=x[j+1]
                x[j+1]=temp
    #List is now sorted according to student's marks
    sec_low_lst=[]
    low=x[0][1]     #Since the lowest marks will be of the first person in the list
    #print low
    for student in x:
        if(student[1]>low):
            sec_low_marks=student[1]   #Finding the second lowest marks
            break
    #print sec_low_marks
    for student in x:
        if(student[1]==sec_low_marks):
            sec_low_lst.append(student[0])  #Making a list of students with the second lowest marks
    return sec_low_lst
            
print(SecondHighest(i))
