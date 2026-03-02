def merge_sort(myList):
    if len(myList)>1:
        mid=len(myList)//2
        leftlist=myList[:mid]
        rightlist=myList[mid:]

        merge_sort(leftlist)
        merge_sort(rightlist)

        i=j=k=0

        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                myList[k]=leftlist[i]
                i+=1
            else:
                myList[k]=rightlist[j]
                j+=1
            k+=1
        
        while i<len(leftlist):
            myList[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            myList[k]=rightlist[j]
            j+=1
            k+=1




l=[1,23,5,753,467,843,46,32,85,26,83]
merge_sort(l)
print(l)
