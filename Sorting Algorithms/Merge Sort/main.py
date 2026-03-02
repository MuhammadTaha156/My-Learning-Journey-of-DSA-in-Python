def merge_sort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        leftList=mylist[:mid]
        rightList=mylist[mid:]

        merge_sort(leftList)
        merge_sort(rightList)

        i=j=k=0

        while i<len(leftList) and j<len(rightList):
            if leftList[i]<rightList[j]:
                mylist[k]=leftList[i]
                i+=1
            else:
                mylist[k]=rightList[j]
                j+=1
            k+=1
        
        while i<len(leftList):
            mylist[k]=leftList[i]
            i+=1
            k+=1

        while j<len(rightList):
            mylist[k]=rightList[j]
            j+=1
            k+=1




lis=[1,23,5,753,467,843,46,32,85,26,83]
merge_sort(lis)
print(lis)